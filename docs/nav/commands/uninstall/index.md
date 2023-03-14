# Resume

## Usage

```bash
linuxp uninstall --help

=============== Output ===============

usage: linuxp uninstall [-h] -m {package,alias,script} [-t TAG] [-i ITEM] [--sudo] [--debug] [--group]

options:
  -h, --help            show this help message and exit

Usage: linuxp uninstall [OPTIONS]:
  -m {package,alias,script}, --module {package,alias,script}
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

    style arg_u_module fill:#BFD7ED,stroke:#333
    style arg_u_tag fill:#BFD7ED,stroke:#333
    style arg_u_item fill:#BFD7ED,stroke:#333
    style arg_u_sudo fill:#B1D8B7,stroke:#333
    style arg_u_debug fill:#B1D8B7,stroke:#333
    style arg_u_group fill:#B1D8B7,stroke:#333

    style L fill:#ededed,stroke:#333
    style u fill:#ededed,stroke:#333
    style option_u fill:#ededed,stroke:#333
```

</center>
