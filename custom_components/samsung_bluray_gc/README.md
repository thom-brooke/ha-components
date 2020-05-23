# samsung_bluray_gc

Home Assistant "Platform" for older model Samsung BluRay players, controlled via IR -- and,
in this case, through a Global Cache GC-100 device.

This component was developed specifically for the Samsung BD H6500, but other models of
similar vintage should be equally well supported.

## Installation

copy folder to `custom_components` in home assistant configuration directory.

## Usage

Add the following to your `configuration.yaml` file:
```yaml
remote h6500:
  - platform: samsung_bluray_gc
    name: H6500
    host: 192.168.10.99
    gc_name: my_gc100
    gc_addr: '2:1'
```

