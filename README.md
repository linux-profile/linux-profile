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

| #      | Command                    | Param         | Argument              | Param           | Argument      |
|--------|:---------------------------|:--------------|:----------------------| :---------------|:--------------|
| 01     | ``linux_profile init``     |               |                       |                 |               |
| 02     | ``linux_profile add``      | ``--module``  | ``package`` ``alias`` |                 |               |
| 03     | ``linux_profile install``  | ``--module``  | ``package`` ``alias`` | ``--category``  | ``default``   |

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
   
- **Package Name:**
   - You choose

</details>


## File 

<details>
  <summary>[linux_profile.json]</summary>
   
    {
      "package": {
          "default": [
              {
                  "id": "AAD6CFE240944748ADDC999A6BA48FB9",
                  "type": "apt-get",
                  "name": "curl",
                  "url": null,
                  "file": null
              }
          ],
          "music": [
              {
                  "id": "BDCA1EE005C5421E931F3A7C07C57110",
                  "type": "snap",
                  "name": "spotify",
                  "url": null,
                  "file": null
              }
          ],
          "dev": [
              {
                  "id": "74A91CA8E2F24DC28E20B4B99EB4D0EA",
                  "type": "apt-get",
                  "name": "git",
                  "url": null,
                  "file": null
              }
          ]
      },
      "alias": {
          "default": [],
          "dev": [
              {
                  "id": "4EB1C7EA7BAF4A70BC40FE04B7EC7581",
                  "content": "git config --global user.name",
                  "command": "git_name"
              },
              {
                  "id": "5ED4967EF17C4730A26970B20E8D1F14",
                  "content": "git config --global user.email",
                  "command": "git_email"
              }
          ],
          "python": [
              {
                  "id": "88B57A16A13247B4A56CE90E44BFD607",
                  "content": "source venv/bin/activate",
                  "command": "activate"
              },
              {
                  "id": "D4C55E7F64884983A88257CE3DBAB87C",
                  "content": "echo 'Python!'",
                  "command": "py3"
              }
          ]
      },
      "terminal": {
          "default": []
      }
    }
  
  Link: https://raw.githubusercontent.com/MyLinuxProfile/linux-profile-basic/master/docs/linux_profile.json
</details>

**RESOURCES**
- GitHub: https://github.com/MyLinuxProfile/linux-profile-basic
- Docs:   https://linuxprofile.com
