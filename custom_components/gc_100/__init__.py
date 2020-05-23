"""Integration for Global Cache GC-100 devices.

The GC-100 is a modular unit which allows the control of IR, serial, and relay 
devices over TCP/IP.

This component is an "Integration Platform", rather than just a "Platform", because
a single GC-100 is typically used to control several end devices (which will normally
be implemented as individual "Platforms") and their commands must be coordinated.  Bad 
things may happen if two platforms attempt to send commands to the same GC-100 at the 
same time.

This integration creates components for all GC-100's in the home assistant system, and
makes them available (through the 'hass' component) to platforms.
"""

import gc_100
import logging
import voluptuous as vol

from homeassistant.const import CONF_HOST, CONF_NAME, CONF_PORT, EVENT_HOMEASSISTANT_STOP
import homeassistant.helpers.config_validation as cv

DOMAIN = "gc_100"

# The GC-100 port is likely not configurable.
# We define this here in case it is (or becomes so)
DEFAULT_PORT = 4998

_LOGGER = logging.getLogger(__name__)

CONFIG_SCHEMA = vol.Schema(
    {
        DOMAIN: [ vol.Schema(
            {
                vol.Required(CONF_NAME): cv.string,
                vol.Required(CONF_HOST): cv.string,
                vol.Optional(CONF_PORT, default=DEFAULT_PORT): cv.port,
            }
        )]
    },
    extra=vol.ALLOW_EXTRA,
)

async def async_setup(hass, config):
    component_config = config.get(DOMAIN)
    if component_config is None:
        return True

    gc_devices = {}
    
    for device in component_config:
        _LOGGER.info(f"setup GC-100 ({device[CONF_NAME]} on {device[CONF_HOST]}:{device[CONF_PORT]})")
        name = DOMAIN+"."+device[CONF_NAME]
        host = device[CONF_HOST]
        port = device[CONF_PORT]
        gc100x = gc_100.GC100(host, port)
        # @todo: gc100.connect() when we hold the connection open.
        gc_devices[name] = gc100x
        hass.data[name] = gc100x
    
    def cleanup_gc100(event):
        """Stuff to do before stopping."""
        for name, device in gc_devices.items():
            # @todo: gc100.disconnect() when we hold the connection open.
            _LOGGER.info(f"cleaning up gc100 {name}@{device._host}")

    hass.bus.async_listen_once(EVENT_HOMEASSISTANT_STOP, cleanup_gc100)
    
    return True
        
