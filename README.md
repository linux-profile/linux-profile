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
  
| Example            |                     | Wiki page      |
| :----------------: | :-----------------: | :------------: |
| ``package``	     | * [ Fixed argument] | [Module](https://github.com/MyLinuxProfile/linux-profile/wiki/Options#module) |
| ``alias``	         | * [ Fixed argument] | [Module](https://github.com/MyLinuxProfile/linux-profile/wiki/Options#module) |
| ``script``	     | * [ Fixed argument] | [Module](https://github.com/MyLinuxProfile/linux-profile/wiki/Options#module) |

</details>

<details>
<summary>TAG</summary>

| Example            |                       | Wiki page      |
| :----------------: | :-------------------: | :------------: |
| ``whatever``	     | [ Any text argument ] | [Tag](https://github.com/MyLinuxProfile/linux-profile/wiki/Options#tag) |

</details>

<details>
<summary>VALUE</summary>

| Example            |                       | Wiki page      |
| :----------------: | :-------------------: | :------------: |
| ``whatever``	     | [ Any text argument ] | [Value](https://github.com/MyLinuxProfile/linux-profile/wiki/Options#value) |

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

## How to Backup?

- First save the file somewhere like:

        cat ~/linuxp/.config/linux_profile.json > ~/backup_profile.json

- Open in a text editor:

        xdg-open ~/backup_profile.json
        
- Open in Google Chrome browser:

        google-chrome ~/backup_profile.json
        
- Open in Firefox browser:

        firefox ~/backup_profile.json

- Open vi text editor

        vi ~/backup_profile.json

## Profile File 

- Link - [linux_profile.json](https://github.com/MyLinuxProfile/linux-profile/blob/master/docs/linux_profile.json)

## Commit Style
- ⚙️ NO-TASK
- 📝 PEP8
- 📌 ISSUE
- 🪲 BUG
- 📘 DOCS

**RESOURCES**
- GitHub: https://github.com/MyLinuxProfile/linux-profile-basic
- Docs:   https://linuxprofile.com
