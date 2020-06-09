# sony_4kuhd_gc

Home Assistant "Platform" for newer model Sony Ultra HD BluRay players, controlled via IR -- and,
in this case, through a Global Cache GC-100 device.

This component was developed specifically for the Sony UBP-X800M2, but other models of
similar vintage should be equally well supported.

## Installation

copy folder to `custom_components` in home assistant configuration directory.

## Usage

Add the following to your `configuration.yaml` file:
```yaml
remote x800m2:
  - platform: sony_4kuhd_gc
    name: X800M2
    host: 192.168.10.99
    gc_name: my_gc100
    gc_addr: '2:1'
```

