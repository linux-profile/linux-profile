# Resume

Profile file management.

## Usage

```bash
linuxp profile --help

=============== Output ===============

usage: linuxp profile [-h] [--url URL] [--output OUTPUT] [--switch SWITCH]

options:
  -h, --help       show this help message and exit

Usage: linuxp profile [OPTIONS]:
  --url URL        URL to download and sync profile.
  --output OUTPUT  File name to save.
  --switch SWITCH  File name for profile switching.

=============== Output ===============
```

## Flow

<center>

``` mermaid
graph TD
    L[linuxp] -->|type command| p(profile)
    p ---> option_p{arguments}
    option_p --->|add| arg_p_url[url]
    option_p --->|add| arg_p_output[output]
    option_p --->|add| arg_p_switch[switch]
```

</center>