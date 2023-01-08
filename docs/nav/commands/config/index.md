# Resume

Settings file management.

## Usage

```bash
linuxp config --help

=============== Output ===============

usage: linuxp config [-h] [--url URL]

options:
  -h, --help  show this help message and exit

Usage: linuxp config [OPTIONS]:
  --url URL   URL to download and sync config.

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