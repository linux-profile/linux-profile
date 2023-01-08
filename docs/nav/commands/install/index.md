# Resume

This parameter is used to install the modules, package, alias and script.

## Usage

```bash
linuxp install --help

=============== Output ===============

usage: linuxp install [-h] -m {package,alias,script,file} [-t TAG] [-i ITEM] [--sudo {on,of}] [--debug {on,of}]

optional arguments:
  -h, --help            show this help message and exit

Usage: linuxp install [OPTIONS]:
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
    L[linuxp] -->|type command| i(install)
    i ---> option_i{arguments}
    option_i --->|add| arg_i_module[module]
    option_i --->|add| arg_i_tag[tag]
    option_i --->|add| arg_i_item[item]
    option_i --->|add| arg_i_sudo[sudo]
    option_i --->|add| arg_i_debug[debug]
```

</center>