# Resume

Lists all modules in the terminal and can also apply filters to find items.

## Usage


```bash
linuxp list --help

=============== Output ===============

usage: linuxp list [-h] -m {package,alias,script,text} [-t TAG] [-i ITEM]

options:
  -h, --help            show this help message and exit

Usage: linuxp list [OPTIONS]:
  -m {package,alias,script,text}, --module {package,alias,script,text}
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

    style arg_l_module fill:#BFD7ED,stroke:#333
    style arg_l_tag fill:#BFD7ED,stroke:#333
    style arg_l_item fill:#BFD7ED,stroke:#333

    style L fill:#ededed,stroke:#333
    style l fill:#ededed,stroke:#333
    style option_l fill:#ededed,stroke:#333
```

</center>