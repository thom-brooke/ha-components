import asyncio
import errno
import gc_100
from homeassistant import util
from homeassistant.components import remote
from homeassistant.components.remote import PLATFORM_SCHEMA
from homeassistant.const import CONF_HOST, CONF_NAME, CONF_PORT, DEVICE_DEFAULT_NAME
import homeassistant.helpers.config_validation as cv
import voluptuous as vol
import logging
import socket
# from tcb_integration import DOMAIN as GC100_DOMAIN

from .ir_codes import CARRIER_FREQUENCY, IR_CODES, REPEAT_OFFSET

_LOGGER = logging.getLogger(__name__)

# we'd like to "import" this, but its location is ... confused.
GC100_DOMAIN = "gc_100"


# @todo:  Remove this "low level" control to a library.  Or find a library which does it.
async def tcp_ping(host, port):
    """TCP "ping".
    
    Not all devices respond to ICMP traffic.  And even for those that do, the client needs 
    elevated privileges to send the "raw" packet.  Using TCP alleviates this, but at some 
    risk of interference.

    To "ping" a host via TCP we simply attempt to open a connection to the host.  If we can
    establish the session, the host is "up"; if we can't because the host refused the connection,
    then it's also "up".  However, if the connection fails because the host isn't found, the host
    is "down".

    There can be some ambiguity if the host simply ignores the connection request.
    There can be some interference if the ping uses a port on which the host is actually listening.
    """
    # to slap a timeout on the open_connection, we need a "future"
    # (can't do it directly.  don't know why not)
    fut = asyncio.open_connection(host=host, port=port)
    try:
        r, w = await asyncio.wait_for(fut, timeout=1)
        w.close()
        await w.wait_closed()
        return True
    except asyncio.TimeoutError:
        # no response
        return False
    except OSError as err:
        if err.errno == errno.ECONNREFUSED:
            # connection refused, but 'host' is still "up"
            return True
        elif err.errno == errno.EHOSTUNREACH:
            # can't find host; not "up"
            return False


# Validation of the user's configuration
PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Required('gc_name'): cv.string,
    vol.Required('gc_addr'): cv.string,
    vol.Required(CONF_HOST): cv.string, # device IP (for "up" test)
    vol.Optional(CONF_PORT, default="1234"): cv.port, # for TCP "ping"
    vol.Optional(CONF_NAME, default=DEVICE_DEFAULT_NAME): cv.string
})


async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    _LOGGER.debug(f"setup samsung with config->{config}")
    host = config.get(CONF_HOST)
    port = config.get(CONF_PORT)
    gc_name = config.get('gc_name')
    gc_addr = config.get('gc_addr')
    name = config.get(CONF_NAME)

    gc100_device = GC100_DOMAIN + "." + gc_name
    gc100 = hass.data.get(gc100_device)
    if gc100 is None:
        _LOGGER.error(f"can't find ->{gc100_device}<- in hass.data")
        return
    async_add_entities([ SamsungRemote(host, port, gc100, gc_addr, name) ])



class SamsungRemote(remote.RemoteDevice):
    """Home Assistant instance of a Samsung BluRay player, IR control via GC-100"""

    def __init__(self, host, port, gc100, gc_addr, name):
        self._host = host
        self._port = port
        self._gc_addr = gc_addr
        self._name = name
        self._state = None
        self.gc100 = gc100 #gc_100.GC100(self._gc_host, self._gc_port)
        self.gc100_ir = gc_100.IR_out(self.gc100, self._gc_addr)
        # construct static GC-100 command strings for each remote command/key:
        self.commands ={cmd : self.gc100_ir.format_sendir(freq=CARRIER_FREQUENCY, offset=REPEAT_OFFSET, code=onoff) for cmd, onoff in IR_CODES.items()}

    @property
    def should_poll(self):
        # poll the device so we know if it was state changed
        # via an external method, like the physical remote
        return True

    @property
    def name(self):
        return self._name

    async def async_update(self):
        self._state = await tcp_ping(self._host, self._port)

    @property
    def is_on(self):
        """Return true if remote is on."""
        return self._state

    @property
    def device_state_attributes(self):
        """Return device state attributes."""
        return {} # {'extra_attr': 'mumble'}

    async def async_turn_on(self, **kwargs):
        """Turn the remote on."""
        _LOGGER.debug("powering on")
        if self.is_on:
            _LOGGER.debug(f"({self.name}) already on.")
            return
        
        try:
            r = await self.gc100_ir.sendir_raw(self.commands['PLAY'])
            _LOGGER.debug(f"({self.name}) turn_on ->{r}")
        except Exception as e:
            _LOGGER.error(e)

        # Typically, we'd want to update the state here, since we "know" we just
        # turned it on.  However, this may be premature.  It takes some time to "wake up",
        # so any scripts or automations that depend on the BR actually being "up" may fail.
        #
        # It may be desirable to wait here until it really is "up".  TBR.
        
        # self._state = True
        # self.async_schedule_update_ha_state(True)

    async def async_turn_off(self, **kwargs):
        """Turn the remote off."""
        _LOGGER.debug("powering off")
        if not self.is_on:
            _LOGGER.debug(f"({self.name}) already off.")
            return
        
        try:
            r = await self.gc100_ir.sendir_raw(self.commands['POWER_TOGGLE'])
            _LOGGER.debug(f"({self.name}) turn_off ->{r}")
        except Exception as e:
            _LOGGER.error(e)

        # Ditto: "premature"...

        # self._state = False
        # self.async_schedule_update_ha_state(True)

    async def async_send_command(self, command, **kwargs):
        """Send a command to the device."""
        _LOGGER.debug(f"sending command(s) {command} with {kwargs}")
        for com in command:
            try:
                r = await self.gc100_ir.sendir_raw(self.commands[com])
                _LOGGER.debug(f"({self.name}) send_command ({com})->{r}")
                # _LOGGER.debug(f"sending: {self.commands[com]}")
            except Exception as e:
                _LOGGER.error(e)

        # self.async_schedule_update_ha_state(True)
