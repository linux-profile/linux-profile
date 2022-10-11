# linux-profile-basic

![GitHub Org's stars](https://img.shields.io/github/stars/MyLinuxProfile?label=LinuxProfile&style=flat-square)
![GitHub last commit](https://img.shields.io/github/last-commit/MyLinuxProfile/linux-profile-basic?style=flat-square)
![GitHub Pipenv locked Python version](https://img.shields.io/github/pipenv/locked/python-version/MyLinuxProfile/linux-profile?style=flat-square)

# Introduction
Linux Profile is a Linux profile management tool. With this project it is possible, from commands executed in the console, to create a 'json' file to store backup configurations. such as information about installed packages, alias, terminal settings. It also allows with a single command to restore saved configurations.

## Quick Install

    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/MyLinuxProfile/linux-profile/master/scripts/install.sh)"

<hr>

## Getting Started

`linux_profile` installation involves:

### 1. Installing dependencies

| Package Manager    | Command                   |
| :----------------: | :-----------------------: |
| Aptitude	         | `apt install curl git`    |
| DNF	             | `dnf install curl git`    |
| Pacman	         | `pacman -S curl git`      |
| Zypper	         | `zypper install curl git` |


### 2. Downloading linux_profile core

| Method             | Command                                                                                      |
| :----------------: | :------------------------------------------------------------------------------------------: |
| Git   	         | `git clone https://github.com/MyLinuxProfile/linux-profile.git ~/linuxp --branch master` |


### 3. Installing linux_profile
  Add the following to ~/.bashrc:

    export PATH=$PATH":$HOME/linuxp"

<hr>

| #      | Command               | Description                                                                              | Wiki page                    |
|--------|:----------------------|:-----------------------------------------------------------------------------------------| :--------------------------: | 
| 01     | ``linuxp init``       | Initial configuration of profile files and server connection.                            | [Command Init](https://github.com/MyLinuxProfile/linux-profile/wiki/Command---Init) |
| 02     | ``linuxp add``        | Parameter used to add a new item to the list in your profile file.                       | [Command Add](https://github.com/MyLinuxProfile/linux-profile/wiki/Command--Add) |
| 03     | ``linuxp install``    | This parameter is used to install the modules, **package**, **alias** and **script**.    | [Command Install](https://github.com/MyLinuxProfile/linux-profile/wiki/Command-Install) |
| 04     | ``linuxp uninstall``  | Command used to uninstall items. Be **very careful** when running.                       | [Command Uninstall](https://github.com/MyLinuxProfile/linux-profile/wiki/Command--Uninstall) |
| 05     | ``linuxp list``       | Lists all modules in the terminal and can also apply filters to find items.              | [Command List](https://github.com/MyLinuxProfile/linux-profile/wiki/Command-List) |

## Commands

<details>
  <summary>INIT</summary>

  - *Example*: 
      - ``linuxp init``

</details>

<details>
  <summary>ADD</summary>

  - *Example*: 
      - ``linuxp add``
          - *Expected parameters*:
              - ``--module`` * [ Required Parameter ]

</details>

<details>
  <summary>INSTALL</summary>

  - *Example*: 
      - ``linuxp install``
          - *Expected parameters*:
              - ``--module`` * [ Required Parameter ]
              - ``--tag`` 
              - ``--value`` 

</details>

<details>
  <summary>UNINSTALL</summary>

  - *Example*: 
      - ``linuxp uninstall``
          - *Expected parameters*:
              - ``--module`` * [ Required Parameter ]
              - ``--tag``

</details>

<details>
  <summary>LIST</summary>

  - *Example*: 
      - ``linuxp list``
          - *Expected parameters*:
              - ``--module`` * [ Required Parameter ]
              - ``--tag`` 
              - ``--value`` 

</details>

## Options:
  
<details>
<summary>MODULE</summary>
  
- *Example*: 
  - ``package`` * [ Fixed argument ]
  - ``alias`` * [ Fixed argument ]
  - ``script`` * [ Fixed argument ]

</details>

<details>
<summary>TAG</summary>

- *Example*: 
  - ``whatever``

</details>

<details>
<summary>VALUE</summary>

- *Example*: 
  - ``whatever``

</details>

## Arguments:

<details>
  <summary>COMMAND: linuxp add --module package</summary>

- **PACKAGE tag [DEFAULT]**:
    - *Example*: 
        - ``You choose``

- **PACKAGE MANAGER:** * [ Option Required ]
    - *Example*: 
        - ``apt-get`` * [ Fixed argument ]
        - ``apt`` * [ Fixed argument ]
        - ``snap`` * [ Fixed argument ]
        - ``deb`` * [ Fixed argument ]
        - ``shell`` * [ Fixed argument ]
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

- **ALIAS tag [DEFAULT]:**:
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

- **SCRIPT tag [DEFAULT]:**:
    - *Example*: 
        - ``You choose``

- **SCRIPT TYPE:** * [ Option Required ]
    - *Example*: 
        - ``shell`` * [ Fixed argument ]
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
                    "tag": "util",
                    "type": "apt",
                    "name": "curl",
                    "url": null,
                    "file": null
                }
            ],
            "dev": [
                {
                    "id": "6826AB807A114923BE4CDDAF5FFE5CD0",
                    "tag": "dev",
                    "type": "apt",
                    "name": "git",
                    "url": null,
                    "file": null
                },
                {
                    "id": "9C3D83B360FF498CBDA02CA7DE12E440",
                    "tag": "dev",
                    "type": "apt",
                    "name": "python3-pip",
                    "url": null,
                    "file": null
                }
            ],
            "music": [
                {
                    "id": "B304C96D5E6A4E92A884B0845EDD0885",
                    "tag": "music",
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
                    "tag": "git",
                    "command": "giename",
                    "body": "git config --global user.name 'LinuxProfile'",
                    "type": "exec"
                },
                {
                    "id": "E345D563A2CB495780B7F41156ED80EA",
                    "tag": "git",
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
                    "tag": "dev",
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
                    "tag": "dev",
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

## How to Backup?

- First save the file somewhere like:

        cat ~/linuxp/.config/linux_profile.json > ~/backup_profile.json

- Open in a text editor:

        xdg-open ~/backup_profile.json
        
- Open in Google Chrome browser:

        google-chrome ~/backup_profile.json
        
- Open in Firefox browser:

        firefox ~/backup_profile.json

## Commit Style
- ⚙️ NO-TASK
- 📝 PEP8
- 📌 ISSUE
- 🪲 BUG
- 📘 DOCS

**RESOURCES**
- GitHub: https://github.com/MyLinuxProfile/linux-profile-basic
- Docs:   https://linuxprofile.com
