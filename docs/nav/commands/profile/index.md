# Resume

Profile file management.

## Usage

```bash
linuxp profile --help

=============== Output ===============

usage: linuxp profile [-h] [--get GET]

options:
  -h, --help  show this help message and exit

Usage: linuxp profile [OPTIONS]:
  --get GET   URL of your profile file to download and sync.

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