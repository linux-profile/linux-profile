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
              "music": [
                  {
                      "id": "BDCA1EE005C5421E931F3A7C07C57110",
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
                      "id": "74A91CA8E2F24DC28E20B4B99EB4D0EA",
                      "is_valid": true,
                      "category": "dev",
                      "type": "apt-get",
                      "name": "git",
                      "url": null,
                      "file": null
                  }
              ],
              "util": [
                  {
                      "id": "AAD6CFE240944748ADDC999A6BA48FB9",
                      "is_valid": true,
                      "category": "util",
                      "type": "apt-get",
                      "name": "curl",
                      "url": null,
                      "file": null
                  }
              ]
          },
          "alias": {
              "dev": [
                  {
                      "id": "4EB1C7EA7BAF4A70BC40FE04B7EC7581",
                      "is_valid": true,
                      "category": "dev",
                      "command": "git_name",
                      "content": "git config --global user.name",
                      "type": "exec"
                  },
                  {
                      "id": "5ED4967EF17C4730A26970B20E8D1F14",
                      "is_valid": true,
                      "category": "dev",
                      "command": "git_email",
                      "content": "git config --global user.email",
                      "type": "exec"
                  }
              ],
              "python": [
                  {
                      "id": "88B57A16A13247B4A56CE90E44BFD607",
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
