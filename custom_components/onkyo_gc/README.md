# onkyo_gc

Home Assistant "Platform" for older model Onkyo AV receivers, controlled via RS-232 (serial) -- and, in this case, through a Global Cache GC-100 device.

This component was developed specifically for the Onkyo TX-SR805, but other models of
similar vintage should be equally well supported.

## Installation

copy folder to `custom_components` in the home assistant configuration directory.

## Usage

Add the following to your `configuration.yaml` file:
```yaml
media_player sr805:
  - name: TX-SR805
    platform: onkyo_gc
    gc_name: my_gc100
    gc_addr: '1:1'
    gc_index: 0
```

You may override the text or label for source inputs via the "inputs" configuration variable.  The map index is the input code (two digit hex string) as defined for the "SLI" command:
```yaml
media_player sr805:
  - name: TX-SR805
    platform: onkyo_gc
    gc_name: my_gc100
    gc_addr: '1:1'
    gc_index: 0
    inputs:
      '01': 'TV/Roku'
      '10': 'Panasonic BR'
      '03': 'Samsung BR'
```

You may override the now-playing background images for source inputs via the "images" configuration variable.  The map index is the input code (two digit hex string) as defined for the "SLI" command.  Image file names are relative to the "www" folder in the home assistant configuration directory:
```yaml
media_player sr805:
  - name: TX-SR805
    platform: onkyo_gc
    gc_name: my_gc100
    gc_addr: '1:1'
    gc_index: 0
    images:
      '01': 'mp-roku.png'
      '10': 'mp-panasonic_br.png'
      '03': 'mp-samsung_br.png'
```

