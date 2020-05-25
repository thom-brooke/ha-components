import asyncio
from homeassistant import util
from homeassistant.components import remote
from homeassistant.components.remote import PLATFORM_SCHEMA
from homeassistant.const import CONF_HOST, CONF_NAME, CONF_PORT, DEVICE_DEFAULT_NAME
from homeassistant.helpers import config_validation as cv, entity_platform, service
from homeassistant.helpers.config_validation import make_entity_service_schema

import voluptuous as vol
import logging

_LOGGER = logging.getLogger(__name__)

# Domain for this platform (vs. the integration itself)
DOMAIN = "dr_ha"

RAM_SCHEMA = make_entity_service_schema({vol.Optional('store'): cv.string})
LOG_SCHEMA = make_entity_service_schema({vol.Required('message'): cv.string})
                                         
# Validation of the user's configuration
PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Optional(CONF_NAME, default=DEVICE_DEFAULT_NAME): cv.string,
    vol.Optional('on_delay', default=0): int
})


async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    _LOGGER.debug(f"setup platform with config->{config}")
    name = config.get(CONF_NAME)
    on_delay = config.get('on_delay')

    platform = entity_platform.current_platform.get()
    platform.async_register_entity_service("set_foo", RAM_SCHEMA, "set_foo_memory")
    platform.async_register_entity_service("set_bar", RAM_SCHEMA, "set_bar_memory")
    platform.async_register_entity_service("logger", LOG_SCHEMA, "log_trace")
    
    async_add_entities([ DiagnosticRemote(name, on_delay) ])



class DiagnosticRemote(remote.RemoteDevice):
    """Home Assistant instance of a Diagnostic platform"""

    IS_ON = 'on'
    IS_OFF = 'off'
    IS_ONING = 'turn-on'
    IS_OFFING = 'turn-off'
    
    def __init__(self, name, on_delay):
        self._name = name
        self._on_delay = on_delay
        self._event_counter = 0
        self._state = {
            'power': None,
            'updates': 0,
            'foo': None,
            'bar': None
        }

    async def state_timer(self, sec, old, new):
        '''Set a timer for 'sec' seconds, then change state from 'old' to 'new'.
        '''
        self._event_counter += 1
        event_num = self._event_counter
        _LOGGER.debug(f"({self.name}) set timer {event_num} for {sec} seconds")
        await asyncio.sleep(sec)
        if self._state['power'] == old:
            _LOGGER.debug(f"({self.name}) timer {event_num} elapsed: update '{old}' -> '{new}'")
            self._state['power'] = new
            self.async_schedule_update_ha_state()
        else:
            _LOGGER.debug(f"({self.name}) timer {event_num} elapsed: expected '{old}' (found '{new}')")
        
    @property
    def should_poll(self):
        # poll the device so we know if it was state changed
        # via an external method, like the physical remote
        return False

    @property
    def name(self):
        return self._name

    @property
    def is_on(self):
        """Return true if remote is on."""
        return self._state['power'] == self.IS_ON

    @property
    def device_state_attributes(self):
        """Return device state attributes."""
        return self._state

    async def async_added_to_hass(self):
        _LOGGER.debug(f"({self.name}) adding to HA")
        await asyncio.sleep(0)
        self.async_schedule_update_ha_state(True)

    async def async_will_remove_from_hass(self):
        # there appears to be a problem with HA not calling this function.
        # make sure things "work" even without it.
        _LOGGER.debug(f"({self.name}) removing from HA")
        await asyncio.sleep(0)

    async def async_update(self):
        _LOGGER.debug(f"({self.name}) update")
        self._state['updates'] += 1
        if self._state['power'] is None:
            self._state['power'] = self.IS_OFF
        await asyncio.sleep(0)

    async def async_turn_on(self, **kwargs):
        """Turn the remote on."""
        _LOGGER.info(f"({self.name}) turn-on.  (Was '{self._state['power']}')")
        if self._state['power'] in (self.IS_ON, self.IS_ONING):
            # nothing to do; already on (or turning on).
            pass
        elif self._state['power'] == self.IS_OFFING:
            # stop turning off and stay on.
            self._state['power'] = self.IS_ON
        elif self._state['power'] == self.IS_OFF:
            # start turning on
            self._state['power'] = self.IS_ONING
            self.hass.async_create_task(self.state_timer(self._on_delay, self.IS_ONING, self.IS_ON))
        else:
            _LOGGER.debug(f"({self.name}) turn-on unexpected power state ->{self._state['power']}<-")
            self._state['power'] = self.IS_OFF
        await asyncio.sleep(0)
        self.async_schedule_update_ha_state()

    async def async_turn_off(self, **kwargs):
        """Turn the remote off."""
        _LOGGER.info(f"({self.name}) turn-off.  (Was '{self._state['power']}')")
        if self._state['power'] in (self.IS_OFF, self.IS_OFFING):
            # nothing to do; already off (or turning off).
            pass
        elif self._state['power'] == self.IS_ONING:
            # stop turning on and stay off.
            self._state['power'] = self.IS_OFF
        elif self._state['power'] == self.IS_ON:
            # start turning off:
            self._state['power'] = self.IS_OFFING
            self.hass.async_create_task(self.state_timer(self._on_delay, self.IS_OFFING, self.IS_OFF))
        else:
            _LOGGER.debug(f"({self.name}) turn-off unexpected power state ->{self._state['power']}<-")
            self._state['power'] = self.IS_OFF
        await asyncio.sleep(0)
        self.async_schedule_update_ha_state()

    async def async_send_command(self, command, **kwargs):
        """Send a command to the device."""
        _LOGGER.info(f"({self.name}) send command(s) ->{command}<-")
        for com in command:
            _LOGGER.debug(f"({self.name}) command ->{com}<-")
            # @todo: look at command and update state
            await asyncio.sleep(0)
        self.async_schedule_update_ha_state()

    def set_foo_memory(self, store="WTF?"):
        _LOGGER.info(f"({self.name}) adjust foo ->{store}<-")
        self._state['foo'] = store
        self.async_schedule_update_ha_state()

    def set_bar_memory(self, store="WTF?"):
        _LOGGER.info(f"({self.name}) adjust bar ->{store}<-")
        self._state['bar'] = store
        self.async_schedule_update_ha_state()

    def log_trace(self, message):
        _LOGGER.info(f"({self.name}): {message}")
        
