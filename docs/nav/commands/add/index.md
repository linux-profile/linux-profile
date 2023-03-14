# Resume

Parameter used to add a new item to the list in your profile file.

## Usage

```bash
linuxp add --help

=============== Output ===============

usage: linuxp add [-h] -m {package,alias,script,text}

options:
  -h, --help            show this help message and exit

Usage: linuxp add [OPTIONS]:
  -m {package,alias,script,text}, --module {package,alias,script,text}

=============== Output ===============
```

## Flow

<center>

``` mermaid
graph TD
    L[linuxp] -->|type command| a(add)
    a ---> option_a{arguments}
    option_a --->|add| arg_a_module[module]

    style arg_a_module fill:#BFD7ED,stroke:#333

    style L fill:#ededed,stroke:#333
    style a fill:#ededed,stroke:#333
    style option_a fill:#ededed,stroke:#333
```

</center>