# linux-profile-basic

![GitHub Org's stars](https://img.shields.io/github/stars/MyLinuxProfile?label=LinuxProfile&style=flat-square)
![GitHub last commit](https://img.shields.io/github/last-commit/MyLinuxProfile/linux-profile-basic?style=flat-square)
![GitHub Pipenv locked Python version](https://img.shields.io/github/pipenv/locked/python-version/MyLinuxProfile/linux-profile?style=flat-square)

# Introduction
Linux Profile is a Linux profile management tool. With this project it is possible, from commands executed in the console, to create a 'json' file to store backup configurations. such as information about installed packages, alias, terminal settings. It also allows with a single command to restore saved configurations.

## Getting Started

`linux_profile` installation involves:

<details>
  <summary>1 - Installing dependencies</summary>
  <br>

| Package Manager    | Command                   |
| :----------------: | :-----------------------: |
| Aptitude	         | `apt install curl git`    |
| DNF	             | `dnf install curl git`    |
| Pacman	         | `pacman -S curl git`      |
| Zypper	         | `zypper install curl git` |

</details>

<details>
  <summary>2 - Downloading linux_profile core</summary>
  <br>

| Method             | Command                                                                                      |
| :----------------: | :------------------------------------------------------------------------------------------: |
| Git   	         | `git clone https://github.com/MyLinuxProfile/linux-profile-basic.git ~/linuxp --branch master` |

</details>

<details>
  <summary>3 - Installing linux_profile</summary>
  <br>
  Add the following to ~/.bashrc:

    export PATH=$PATH":$HOME/linuxp"

</details>

## Quick Install

    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/MyLinuxProfile/linux-profile-basic/master/scripts/install.sh)"

## Commands

| #      | Command               |
|--------|:----------------------|
| 01     | ``linuxp init``       |
| 02     | ``linuxp add``        |
| 03     | ``linuxp install``    |
| 04     | ``linuxp uninstall``  |

## Params:

1. - **INIT** - Initial configuration of profile files and server connection.
    - *Example*: 
        - ``linuxp init``

2. - **ADD**
    - *Example*: 
        - ``linuxp add``
            - *Expected parameters*:
                - ``--module`` * [ Required Parameter ]

3. - **INSTALL**
    - *Example*: 
        - ``linuxp install``
            - *Expected parameters*:
                - ``--module`` * [ Required Parameter ]
                - ``--category`` 
                - ``--value`` 

4. - **UNINSTALL**
    - *Example*: 
        - ``linuxp uninstall``
            - *Expected parameters*:
                - ``--module`` * [ Required Parameter ]
                - ``--category``

## Arguments:

1. - **--MODULE**
    - *Example*: 
        - ``package`` * [ Fixed argument ]
        - ``alias`` * [ Fixed argument ]
        - ``script`` * [ Fixed argument ]

2. - **--CATEGORY**
    - *Example*: 
        - ``whatever``

2. - **--VALUE**
    - *Example*: 
        - ``whatever``

## Options:

<details>
  <summary>COMMAND: linuxp add --module package</summary>

- **PACKAGE CATEGORY [DEFAULT]**:
    - *Example*: 
        - ``You choose``

- **PACKAGE MANAGER:** * [ Option Required ]
    - *Example*: 
        - ``apt-get`` * [ Fixed argument ]
        - ``apt`` * [ Fixed argument ]
        - ``snap`` * [ Fixed argument ]
        - ``deb`` * [ Fixed argument ]
        - ``sh`` * [ Fixed argument ]
        - ``py`` * [ Fixed argument ]
        - ``dnf`` * [ Fixed argument ]
        - ``pacman`` * [ Fixed argument ]
        - ``zypper`` * [ Fixed argument ]
        - ``spack`` * [ Fixed argument ]
        - ``brew`` * [ Fixed argument ]
        - ``pip`` * [ Fixed argument ]

- **PACKAGE NAME:** * [ Option Required ]
    - *Example*: 
        - ``You choose``

</details>

<details>
  <summary>COMMAND: linuxp add --module alias</summary>

- **ALIAS CATEGORY [DEFAULT]:**:
    - *Example*: 
        - ``You choose``

- **ALIAS COMMAND:** * [ Option Required ]
    - *Example*: 
        - ``You choose``

- **ALIAS BODY:** * [ Option Required ]
    - *Example*: 
        - ``You choose``

</details>

<details>
  <summary>COMMAND: linuxp add --module script</summary>

- **SCRIPT CATEGORY [DEFAULT]:**:
    - *Example*: 
        - ``You choose``

- **SCRIPT TYPE:** * [ Option Required ]
    - *Example*: 
        - ``bash`` * [ Fixed argument ]
        - ``python`` * [ Fixed argument ]
        - ``python3`` * [ Fixed argument ]
        - ``ruby`` * [ Fixed argument ]

- **SCRIPT NAME:** * [ Option Required ]
    - *Example*: 
        - ``You choose``

- **SCRIPT SHEBANG:**
    - *Example*: 
        - ``#!/bin/bash``
        - ``#!/usr/bin/env python``
        - ``#!/usr/bin/env python3``
        - ``#!/usr/bin/env ruby``

- **SCRIPT BODY:** * [ Option Required ]
    - *Example*: 
        - ``echo 'LinuxProfile!'``

</details>

## File 

<details>
  <summary>[linux_profile.json]</summary>
   
    {
        "package": {
            "util": [
                {
                    "id": "E07BB00A71C14FF3878153A329745974",
                    "category": "util",
                    "type": "apt",
                    "name": "curl",
                    "url": null,
                    "file": null
                }
            ],
            "dev": [
                {
                    "id": "6826AB807A114923BE4CDDAF5FFE5CD0",
                    "category": "dev",
                    "type": "apt",
                    "name": "git",
                    "url": null,
                    "file": null
                },
                {
                    "id": "9C3D83B360FF498CBDA02CA7DE12E440",
                    "category": "dev",
                    "type": "apt",
                    "name": "python3-pip",
                    "url": null,
                    "file": null
                }
            ],
            "music": [
                {
                    "id": "B304C96D5E6A4E92A884B0845EDD0885",
                    "category": "music",
                    "type": "snap",
                    "name": "spotify",
                    "url": null,
                    "file": null
                }
            ]
        },
        "alias": {
            "git": [
                {
                    "id": "02BEF934DC8E4D0F90766C24320E0778",
                    "category": "git",
                    "command": "giename",
                    "body": "git config --global user.name 'LinuxProfile'",
                    "type": "exec"
                },
                {
                    "id": "E345D563A2CB495780B7F41156ED80EA",
                    "category": "git",
                    "command": "giename",
                    "body": "git config --global user.email 'email@linuxprofile.com'",
                    "type": "exec"
                }
            ]
        },
        "script": {
            "dev": [
                {
                    "id": "63982A972A4C460C881714FF1EE6C391",
                    "category": "dev",
                    "type": "sh",
                    "name": "install_poetry",
                    "body": [
                        "#!/bin/bash",
                        "",
                        "sudo apt install curl git",
                        "curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -"
                    ]
                },
                {
                    "id": "0238BB34E0AC44CAAA0E35C5E8335787",
                    "category": "dev",
                    "type": "sh",
                    "name": "install_asdf",
                    "body": [
                        "#!/bin/bash",
                        "",
                        "sudo apt install curl git",
                        "git clone https://github.com/asdf-vm/asdf.git ~/.asdf --branch v0.10.2",
                        "echo '. $HOME/.asdf/asdf.sh' >> ~/.bashrc",
                        "echo '. $HOME/.asdf/completions/asdf.bash' >> ~/.bashrc"
                    ]
                }
            ]
        }
    }
  
  Link: https://raw.githubusercontent.com/MyLinuxProfile/linux-profile-basic/master/docs/linux_profile.json
</details>

## Commit Style
- ⚙️ NO-TASK
- 📝 PEP8
- 📌 ISSUE
- 🪲 BUG
- 📘 DOCS

**RESOURCES**
- GitHub: https://github.com/MyLinuxProfile/linux-profile-basic
- Docs:   https://linuxprofile.com
