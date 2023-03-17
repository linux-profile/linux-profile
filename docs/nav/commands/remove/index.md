# Resume

Removes items from the profile file.

## Usage

```bash
linuxp remove --help

=============== Output ===============

usage: linuxp remove [-h] --id ID

options:
  -h, --help  show this help message and exit

Usage: linuxp remove [OPTIONS]:
  --id ID     Reference ID of a storage item.

=============== Output ===============
```

## Flow

<center>

``` mermaid
graph TD
    L[linuxp] -->|type command| r(remove)
    r ---> option_r{arguments}
    option_r --->|add| arg_r_id[id]

    style arg_r_id fill:#BFD7ED,stroke:#333
  
    style L fill:#ededed,stroke:#333
    style r fill:#ededed,stroke:#333
    style option_r fill:#ededed,stroke:#333
```

</center>