# dr_ha

Home Assistant "Platform" for debugging and diagnostics.

How does this crap _really_ work?  It's certainly not clear from the documentation.
So this component simply logs what it's doing, and keeps track of how/when some
interfaces are called.

Use this as a testbed for "fragile" hardware, where you don't really want to experiment
with the real equipment (e.g., a video projector, whose bulb life is limited and expensive
to replace -- what with constant turning on and off).

## Installation

Copy the `dr_ha` folder to `custom_components` in the home assistant configuration directory.

## Usage

Add the following to your `configuration.yaml` file:
```yaml
remote foo:
  - platform: dr_ha
    name: mumble
```

You can add a delay (in seconds) between when you turn the entity on (or off) and when it reports that it actually is on (or off):
```yaml
remote bar:
  - platform: dr_ha
    name: snooze
    on_delay: 5
```

You may notice ... eccentric ... UI behavior when `on_delay` is non-zero.

The `dr_ha` platform exposes the following services:
 * `logger` writes a message to the log.
 * `set_foo` stores a value in the entity's `foo` attribute.
 * `set_bar` stores a value in the entity's `bar` attribute.
 