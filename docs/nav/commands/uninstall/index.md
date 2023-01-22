# Resume

## Usage

```bash
linuxp uninstall --help

=============== Output ===============

usage: linuxp uninstall [-h] -m {package,alias,script,file} [-t TAG] [-i ITEM] [--sudo] [--debug] [--group]

options:
  -h, --help            show this help message and exit

Usage: linuxp uninstall [OPTIONS]:
  -m {package,alias,script,file}, --module {package,alias,script,file}
  -t TAG, --tag TAG
  -i ITEM, --item ITEM
  --sudo                Run the command with system root permissions.
  --debug               Run a command in test mode. It only shows the command.
  --group               Group items for executing a command.

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
    option_u --->|add| arg_u_group[group]
```

</center>
