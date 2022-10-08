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

| #      | Command                      | Param         | Argument                          | Param           | Argument      |
|--------|:-----------------------------|:--------------|:----------------------------------| :---------------|:--------------|
| 01     | ``linux_profile init``       |               |                                   |                 |               |
| 02     | ``linux_profile add``        | ``--module``* | ``package`` ``alias`` ``script``  |                 |               |
| 03     | ``linux_profile install``    | ``--module``* | ``package`` ``alias``             | ``--category``  | ``default``   |
| 04     | ``linux_profile uninstall``  | ``--module``* | ``package`` ``alias``             | ``--category``* | ``default``   |

## Options:
<details>
  <summary>COMMAND: linux_profile add --module package</summary>

- **Package Category [default]**:
   - You choose

- **Package Manager:**
   - apt-get
   - apt
   - snap
   - deb
   - sh
   - py
   - dnf
   - pacman
   - zypper
   - spack
   - brew
   - pip
   
- **Package Name:**
   - You choose

</details>


## File 

<details>
  <summary>[linux_profile.json]</summary>
   
      {
          "package": {
              "music": [
                  {
                      "id": "8394F3F8EC4A4BC1AE026FEC834D8641",
                      "is_valid": true,
                      "category": "music",
                      "type": "snap",
                      "name": "spotify",
                      "url": null,
                      "file": null
                  }
              ],
              "dev": [
                  {
                      "id": "3A892C46F1FA46BCAF825D47B70D813F",
                      "is_valid": true,
                      "category": "dev",
                      "type": "apt",
                      "name": "git",
                      "url": null,
                      "file": null
                  }
              ],
              "util": [
                  {
                      "id": "4D48DBE688C344D5866B0FD93813EE9E",
                      "is_valid": true,
                      "category": "util",
                      "type": "apt",
                      "name": "curl",
                      "url": null,
                      "file": null
                  }
              ]
          },
          "alias": {
              "dev": [
                  {
                      "id": "78EC0EB1EAC14C2FA755892D222FD48C",
                      "is_valid": true,
                      "category": "dev",
                      "command": "git_name",
                      "content": "git config --global user.name",
                      "type": "exec"
                  },
                  {
                      "id": "FE1E8CCA2DEF479F8AAC3BDE35827A07",
                      "is_valid": true,
                      "category": "dev",
                      "command": "git_email",
                      "content": "git config --global user.email",
                      "type": "exec"
                  }
              ],
              "python": [
                  {
                      "id": "AC640AFF20E5455A80BF1AFECD3FF7B9",
                      "is_valid": true,
                      "category": "python",
                      "command": "activate",
                      "content": "source venv/bin/activate",
                      "type": "exec"
                  }
              ]
          }
      }
  
  Link: https://raw.githubusercontent.com/MyLinuxProfile/linux-profile-basic/master/docs/linux_profile.json
</details>

## Commits
- ⚙️ NO-TASK
- 📝 PEP8
- 📌 ISSUE
- 🪲 BUG

**RESOURCES**
- GitHub: https://github.com/MyLinuxProfile/linux-profile-basic
- Docs:   https://linuxprofile.com
