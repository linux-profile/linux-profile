# Resume

Settings file management.

## Usage

```bash
linuxp config --help

=============== Output ===============

usage: linuxp config [-h] [--get GET]

options:
  -h, --help  show this help message and exit

Usage: linuxp config [OPTIONS]:
  --get GET   URL of your settings file to download and sync.

=============== Output ===============
```

## Flow

<center>

``` mermaid
graph TD
    L[linuxp] -->|type command| c(config)
    c ---> option_c{arguments}
    option_c --->|add| arg_c_url[url]
```

</center>