# Resume

Profile file management.

## Usage

```bash
linuxp profile --help

=============== Output ===============

usage: linuxp profile [-h] [--url URL] [--output OUTPUT] [--switch SWITCH] [--new NEW] [--delete DELETE] [--list]

options:
  -h, --help       show this help message and exit

Usage: linuxp profile [OPTIONS]:
  --url URL        URL to download and sync profile.
  --output OUTPUT  File name to save.
  --switch SWITCH  File name for profile switching.
  --new NEW        Creates a new profile.
  --delete DELETE  Deletes a profile.
  --list           Argument to list existing profiles

=============== Output ===============
```

## Flow

<center>

``` mermaid
graph TD
    L[linuxp] -->|type command| p(profile)
    p ---> option_p{arguments}
    option_p --->|add| arg_p_url[url]
    option_p --->|add| arg_p_output[output]
    option_p --->|add| arg_p_switch[switch]
    option_p --->|add| arg_p_new[new]
    option_p --->|add| arg_p_delete[delete]
    option_p --->|add| arg_p_list[list]

    style arg_p_url fill:#BFD7ED,stroke:#333
    style arg_p_output fill:#BFD7ED,stroke:#333
    style arg_p_switch fill:#BFD7ED,stroke:#333
    style arg_p_new fill:#BFD7ED,stroke:#333
    style arg_p_delete fill:#BFD7ED,stroke:#333
    style arg_p_list fill:#B1D8B7,stroke:#333

    style L fill:#ededed,stroke:#333
    style p fill:#ededed,stroke:#333
    style option_p fill:#ededed,stroke:#333
```

</center>