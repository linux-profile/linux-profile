# Resume

Settings file management.

## Usage

```bash
linuxp config --help

=============== Output ===============

usage: linuxp config [-h] [--url URL] [--editor EDITOR]

options:
  -h, --help       show this help message and exit

Usage: linuxp config [OPTIONS]:
  --url URL        URL to download and sync config.
  --editor EDITOR  Default text editor

=============== Output ===============
```

## Flow

<center>

``` mermaid
graph TD
    L[linuxp] -->|type command| c(config)
    c ---> option_c{arguments}
    option_c --->|add| arg_c_url[url]
    option_c --->|add| arg_c_editor[editor]

    style arg_c_url fill:#BFD7ED,stroke:#333
    style arg_c_editor fill:#BFD7ED,stroke:#333

    style L fill:#ededed,stroke:#333
    style c fill:#ededed,stroke:#333
    style option_c fill:#ededed,stroke:#333
```

</center>