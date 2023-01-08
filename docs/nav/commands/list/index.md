# Resume

Lists all modules in the terminal and can also apply filters to find items.

## Usage


```bash
linuxp list --help

=============== Output ===============

usage: linuxp list [-h] -m {package,alias,script,file} [-t TAG] [-i ITEM]

optional arguments:
  -h, --help            show this help message and exit

Usage: linuxp list [OPTIONS]:
  -m {package,alias,script,file}, --module {package,alias,script,file}
  -t TAG, --tag TAG
  -i ITEM, --item ITEM

=============== Output ===============
```

## Flow

<center>

``` mermaid
graph TD
    L[linuxp] -->|type command| l(list)
    l ---> option_l{arguments}
    option_l --->|add| arg_l_module[module]
    option_l --->|add| arg_l_tag[tag]
    option_l --->|add| arg_l_item[item]
```

</center>