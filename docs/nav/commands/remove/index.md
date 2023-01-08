# Resume

Removes items from the profile file.

## Usage

```bash
linuxp remove --help

=============== Output ===============

usage: linuxp remove [-h] --id ID

optional arguments:
  -h, --help  show this help message and exit

Usage: linuxp remove [OPTIONS]:
  --id ID     Reference ID of a database item.

=============== Output ===============
```

## Flow

<center>

``` mermaid
graph TD
    L[linuxp] -->|type command| r(remove)
    r ---> option_r{arguments}
    option_r --->|add| arg_r_id[id]
```

</center>