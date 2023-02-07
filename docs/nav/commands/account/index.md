# Resume

Account management.

## Usage

```bash
linuxp account --help

=============== Output ===============

usage: linuxp account [-h] [--signup] [--login]

options:
  -h, --help  show this help message and exit

Usage: linuxp account [OPTIONS]:
  --signup
  --login

=============== Output ===============
```

## Flow

<center>

``` mermaid
graph TD
    L[linuxp] -->|type command| a(account)
    a ---> option_a{arguments}
    option_a --->|add| arg_a_signup[signup]
    option_a --->|add| arg_a_login[login]

    style arg_a_signup fill:#B1D8B7,stroke:#333
    style arg_a_login fill:#B1D8B7,stroke:#333

    style L fill:#ededed,stroke:#333
    style a fill:#ededed,stroke:#333
    style option_a fill:#ededed,stroke:#333
```

</center>