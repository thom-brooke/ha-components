import asyncio
import errno
import gc_100
from . import iscp

from homeassistant import util
import homeassistant as ha
import homeassistant.const

import homeassistant.components.media_player as mp
import homeassistant.components.media_player.const
from homeassistant.components.media_player import PLATFORM_SCHEMA

import homeassistant.helpers.config_validation as cv
import typing
import voluptuous as vol
import logging
# from tcb_integration import DOMAIN as GC100_DOMAIN


_LOGGER = logging.getLogger(__name__)

# we'd like to "import" this, but its location is ... confused.
GC100_DOMAIN = "gc_100"

POWER = b'PWR'
MUTING = b'AMT'
VOLUME = b'MVL'
INPUT = b'SLI'
MODE = b'LMD'

# @todo: supported functions?
SUPPORT_ONKYO = (
    mp.const.SUPPORT_VOLUME_SET
    | mp.const.SUPPORT_VOLUME_STEP
    | mp.const.SUPPORT_VOLUME_MUTE
    | mp.const.SUPPORT_SELECT_SOURCE
    | mp.const.SUPPORT_SELECT_SOUND_MODE
    | mp.const.SUPPORT_TURN_ON
    | mp.const.SUPPORT_TURN_OFF
)


# Validation of the user's configuration
PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Required('gc_name'): cv.string,
    vol.Required('gc_addr'): cv.string,
    vol.Required('gc_index'): int,
    vol.Optional('model', default='TX-SR805'): cv.string,
    vol.Optional('inputs') : { vol.All(cv.string): cv.string },
    vol.Optional('images') : { vol.All(cv.string): cv.string },
    vol.Optional(ha.const.CONF_NAME, default=ha.const.DEVICE_DEFAULT_NAME): cv.string,
})


async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    _LOGGER.debug(f"setup onkyo with config->{config}")
    gc_name = config.get('gc_name')
    gc_addr = config.get('gc_addr')
    gc_index = config.get('gc_index')
    model = config.get('model')
    inputs = config.get('inputs') or {}
    images = config.get('images') or {}
    name = config.get(ha.const.CONF_NAME)

    # @todo register additional services here?

    gc100_device = GC100_DOMAIN + "." + gc_name
    gc100 = hass.data.get(gc100_device)
    if gc100 is None:
        _LOGGER.error(f"can't find ->{gc100_device}<- in hass.data")
        return
    async_add_entities([ OnkyoMediaPlayer(gc100, gc_addr, gc_index, model, name, inputs, images) ])


class OnkyoMediaPlayer(mp.MediaPlayerDevice):
    """Home Assistant instance of an Onkyo A/V Receiver (eISCP), RS232 control via GC-100"""

    def __init__(self, gc100, gc_addr, gc_index, model, name, inputs, images):
        self._gc_addr = gc_addr
        self._gc_index = gc_index
        self._model = model
        self._iscp = iscp.ISCP_device(model)
        for k,v in inputs.items():
            self._iscp.inputs[k] = v
        self._images = {k : None for k in self._iscp.inputs}
        for k,v in images.items():
            self._images[k] = v
        self._name = name
        self._state = {
            POWER: None,
            MUTING: None,
            VOLUME: None,
            INPUT: None,
            MODE: None
        }
        self._running = False
        self.gc100 = gc100
        self.gc100_rs232 = gc_100.Serial(self.gc100, self._gc_addr, self._gc_index)

    async def async_added_to_hass(self):
        _LOGGER.debug(f"adding to hass ({self._name})")
        self._running = True
        try:
            await self.gc100_rs232.connect()
            self._reader = asyncio.create_task(self.onkyo_listener())
        except Exception as e:
            _LOGGER.error(f"{self._name} failed to startup ->{e}")
            self._running = False
        self.async_schedule_update_ha_state(True)

    async def async_will_remove_from_hass(self):
        # there appears to be a problem with HA not calling this function.
        # make sure things "work" even without it.
        _LOGGER.debug(f"removing from hass ({self._name})")
        self._running = False
        try:
            self._reader.cancel()
            await self._reader
            await self.gc100_rs232.disconnect()
        except Exception as e:
            _LOGGER.error(f"{self._name} failed to shutdown ->{e}<-")

    async def async_update(self):
        checks = (iscp.POWER, iscp.VOLUME, iscp.MUTING, iscp.INPUT, iscp.MODE)
        for cmd in checks: 
            await self.onkyo_command(self._iscp.mk_query(cmd))
            await asyncio.sleep(0.1)
        # others?

    @property
    def should_poll(self):
        # We *shouldn't* need to poll, since ISCP sends us notifications
        # on changes.  But we've seen at least once (manual power off) where we
        # didn't get a message.  Poll to catch the corner cases.
        return False

    @property
    def name(self):
        return self._name

    @property
    def is_on(self):
        """Return true if remote is on."""
        return self._state[POWER]

    @property
    def device_state_attributes(self):
        """Return device state attributes."""
        return {
            'power': str(self._state[POWER]),
            'muting': str(self._state[MUTING]),
            'volume': str(self._state[VOLUME]),
            'input': str(self._state[INPUT]),
            'mode': str(self._state[MODE])
        } # self._state

    @property
    def media_content_type(self):
        """Content type of current playing media."""
        input = self.get_source_code(self._state[INPUT])
        if input in iscp.VIDEO_INPUTS:
            return mp.const.MEDIA_TYPE_MOVIE
        return mp.const.MEDIA_TYPE_MUSIC

    @property
    def media_image_url(self):
        """Image url of current playing media."""
        image = None
        code = self.get_source_code(self._state[INPUT])
        if code in self._images:
            image = self._images[code]
        if image is not None:
            return f"/local/{image}"

    @property
    def source(self):
        if self.is_on:
            return self._state[INPUT]

    @property
    def source_list(self):
        return self.get_source_list()
    
    def get_source_list(self):
        return [v for v in self._iscp.inputs.values()]

    def get_source_code(self, source):
        if source is None:
            return None
        return next(k for k,v in self._iscp.inputs.items() if v == source)
    
    @property
    def state(self):
        # _LOGGER.debug(f"check state ({self._name}) -> {self._state[POWER]}")
        if self._state[POWER]:
            return ha.const.STATE_ON
        else:
            return ha.const.STATE_OFF #ha.const.STATE_STANDBY
        
    @property
    def supported_features(self):
        """Flag media player features that are supported."""
        return SUPPORT_ONKYO

    @property
    def volume_level(self):
        """Volume level of the media player (0..1)."""
        return self._state[VOLUME]

    @property
    def is_volume_muted(self):
        """Boolean if volume is currently muted."""
        return self._state[MUTING]

    async def async_turn_on(self, **kwargs):
        """Turn the remote on."""
        _LOGGER.debug("powering on")
        try:
            await self.onkyo_command(self._iscp.mk_command(iscp.POWER, iscp.ON))
        except Exception as e:
            _LOGGER.error(e)
        self._state[POWER] = True
        self.async_schedule_update_ha_state()

    async def async_turn_off(self, **kwargs):
        """Turn the remote off."""
        _LOGGER.debug("powering off")
        try:
            await self.onkyo_command(self._iscp.mk_command(iscp.POWER, iscp.OFF))
        except Exception as e:
            _LOGGER.error(e)
        # If the receiver is already off, we may not receive the "PWR00" response.
        self._state[POWER] = False
        self.async_schedule_update_ha_state()

    async def async_volume_up(self):
        """Volume up media player."""
        if self.is_on:
            try:
                await self.onkyo_command(self._iscp.mk_command(iscp.VOLUME, iscp.UP))
            except Exception as e:
                _LOGGER.error(e)

    async def async_volume_down(self):
        """Volume down media player."""
        if self.is_on:
            try:
                await self.onkyo_command(self._iscp.mk_command(iscp.VOLUME, iscp.DOWN))
            except Exception as e:
                _LOGGER.error(e)

    async def async_mute_volume(self, mute):
        _LOGGER.debug(f"({self._name}) muting ->{mute}<-")
        if self.is_on:
            try:
                await self.onkyo_command(self._iscp.mk_command(iscp.MUTING, iscp.ON if mute else iscp.OFF))
            except Exception as e:
                _LOGGER.error(e)

    async def async_set_volume_level(self, volume):
        _LOGGER.debug(f"({self._name}) set volume level to {volume}")
        if self.is_on:
            try:
                await self.onkyo_command(self._iscp.mk_command(iscp.VOLUME, self._iscp.arg_volume(volume)))
            except Exception as e:
                _LOGGER.error(e)
        
    async def async_select_source(self, source):
        """Select input source."""
        _LOGGER.debug(f"({self._name}) select source ->{source}<-")
        if self.is_on:
            try:
                s = next(k for k,v in self._iscp.inputs.items() if v == source)
                await self.onkyo_command(self._iscp.mk_command(iscp.INPUT, s))
            except StopIteration as e:
                _LOGGER.error(f"({self._name}) source not found ->{source}<-")
            except Exception as e:
                _LOGGER.error(e)

    async def async_select_sound_mode(self, mode):
        _LOGGER.debug(f"({self._name}) select sound mode ->{mode}<-")

        
    async def onkyo_command(self, command):
        _LOGGER.debug(f"({self._name}) send onkyo_command ->{str(command)}<-")
        try:
            await self.gc100_rs232.send(bytes(command, encoding='ascii'))
        except Exception as e:
            _LOGGER.error(f"({self._name}) onkyo_command failed ->{e}<- ({type(e)})")
            raise e
            
    async def process_message(self, msg):
        """Given an ISCP [response] msg, parse it and process it.

        'msg' should be a str with the leading PREFIX but no SUFFIX.
        """
        _LOGGER.debug(f"({self._name}) process msg->{msg}<-")
        op, arg = None, None
        try:
            op, arg = self._iscp.parse(msg)
        except ValueError as e:
            _LOGGER.error(f"({self._name}) bad command in ->{msg}<- ({e})")
            return
        
        if op == iscp.POWER:
            self._state[POWER] = (arg != iscp.OFF)
        elif op == iscp.MUTING:
            self._state[MUTING] = (arg != iscp.OFF)
        elif op == iscp.VOLUME:
            # todo: scale this?
            self._state[VOLUME] = self._iscp.normalize_volume(arg)
        elif op == iscp.INPUT:
            # @todo: map to human-readable (including config override)
            self._state[INPUT] = self._iscp.inputs[arg]
        elif op == iscp.MODE:
            # @todo: map to human-readable
            self._state[MODE] = arg
        else:
            _LOGGER.info(f"({self._name}) unrecognized message format: <{op}> <{arg}>")
        
        self.async_schedule_update_ha_state()
                
    async def onkyo_listener(self):
        pending = ''
        while self._running:
            idx = pending.find(iscp.SUFFIX_MSG)
            if idx != -1:
                # at least one complete message is pending.
                # get it and process it
                msg = pending[0:idx]
                pending = pending[idx+1:]
                # if we get flooded with messages, we don't want to block.
                # allow other tasks to run by spinning off a task to process each one.
                asyncio.create_task(self.process_message(msg))
            else:
                # no complete message/response pending; go get more
                try:
                    data = await self.gc100_rs232.recv(1024)
                    _LOGGER.debug(f"{self._name} onkyo_listener received ->{data}<-")
                    pending += data.decode('ascii')
                except gc_100.SerialError as e:
                    # this is anticipated if the serial connection is lost (e.g., at shutdown)
                    _LOGGER.info(f"{self._name} onkyo_listener serial error: ->{e}<-")
                    break
                except TimeoutError:
                    # this is anticipated if the GC-100 gets confused (e.g., from packets sent too fast).
                    # wait awhile, then reconnect.
                    await self.gc100_rs232.disconnect()
                    await asyncio.sleep(10) # or however long it takes
                    await self.gc100_rs232.connect()
                except Exception as e:
                    _LOGGER.error(f"{self._name} onkyo_listener failed with ->{e}<- ({type(e)})")
                    break
