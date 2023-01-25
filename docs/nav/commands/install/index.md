# Resume

This parameter is used to install the modules, package, alias and script.

## Usage

```bash
linuxp install --help

=============== Output ===============

usage: linuxp install [-h] -m {package,alias,script,file} [-t TAG] [-i ITEM] [--sudo] [--debug] [--group]

options:
  -h, --help            show this help message and exit

Usage: linuxp install [OPTIONS]:
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
    L[linuxp] -->|type command| i(install)
    i ---> option_i{arguments}
    option_i --->|add| arg_i_module[module]
    option_i --->|add| arg_i_tag[tag]
    option_i --->|add| arg_i_item[item]
    option_i --->|add| arg_i_sudo[sudo]
    option_i --->|add| arg_i_debug[debug]
    option_i --->|add| arg_i_group[group]

    style arg_i_module fill:#BFD7ED,stroke:#333
    style arg_i_tag fill:#BFD7ED,stroke:#333
    style arg_i_item fill:#BFD7ED,stroke:#333
    style arg_i_sudo fill:#B1D8B7,stroke:#333
    style arg_i_debug fill:#B1D8B7,stroke:#333
    style arg_i_group fill:#B1D8B7,stroke:#333

    style L fill:#ededed,stroke:#333
    style i fill:#ededed,stroke:#333
    style option_i fill:#ededed,stroke:#333
```

</center>