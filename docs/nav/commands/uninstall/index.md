# Resume

## Usage

```bash
linuxp uninstall --help

=============== Output ===============

usage: linuxp uninstall [-h] -m {package,alias,script,file} [-t TAG] [-i ITEM] [--sudo {on,of}] [--debug {on,of}]

optional arguments:
  -h, --help            show this help message and exit

Usage: linuxp uninstall [OPTIONS]:
  -m {package,alias,script,file}, --module {package,alias,script,file}
  -t TAG, --tag TAG
  -i ITEM, --item ITEM
  --sudo {on,of}        Run the command with system root permissions.
  --debug {on,of}       Run a command in test mode. It only shows the command.

=============== Output ===============
```

## Flow

<center>

``` mermaid
graph TD
    L[linuxp] -->|type command| u(uninstall)
    u ---> option_u{arguments}
    option_u --->|add| arg_u_module[module]
    option_u --->|add| arg_u_tag[tag]
    option_u --->|add| arg_u_item[item]
    option_u --->|add| arg_u_sudo[sudo]
    option_u --->|add| arg_u_debug[debug]
```

</center>
