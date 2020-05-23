# gc_100

Integration for one or more Global Cache GC-100 devices.

## Installation

Put this folder in `custom_components` within the home-assistant configuration directory.

Install the `pygc100` library.  Note that `pygc100` is _not_ available in PyPi, so home assistant can't install it automatically.  It _is_, however, available on Github: https://github.com/thom-brooke/pygc100

## Usage

Add the following to the `configuration.yaml` file:
```yaml
gc_100:
  - name: my_gc100
    host: 192.168.10.11
```

Replace the `name` ("my_gc100") and `host` ("192.168.10.11") with values appropriate
for your home-assistant configuration.

Note that you _should_ define _all_ GC-100 devices under the same `gc_100` entry.
Just give them unique names and host addresses (obviously).

Platforms which are controlled through a GC-100 should reference it by name.
For example, a Panasonic BluRay player with IR control might look something like this:
```yaml
remote bd35:
  - platform: panasonic_bluray_gc
    name: Panasonic BluRay
    host: 192.168.10.99
    gc_name: my_gc100
    gc_addr: '2:1'
```
