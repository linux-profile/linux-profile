# linux-profile

<img src="https://github.com/MyLinuxProfile/linux-profile/blob/master/docs/linuxp.png?raw=true">

![GitHub Org's stars](https://img.shields.io/github/stars/MyLinuxProfile?label=LinuxProfile&style=flat-square)
![GitHub last commit](https://img.shields.io/github/last-commit/MyLinuxProfile/linux-profile?style=flat-square)
![GitHub Pipenv locked Python version](https://img.shields.io/github/pipenv/locked/python-version/MyLinuxProfile/linux-profile?style=flat-square)
![PyPI](https://img.shields.io/pypi/v/linuxp)
![PyPI - Downloads](https://img.shields.io/pypi/dm/linuxp?style=flat-square)

[![check](https://github.com/MyLinuxProfile/linux-profile/actions/workflows/python-publish-pypi.yml/badge.svg)](https://github.com/MyLinuxProfile/linux-profile/actions/workflows/python-publish-pypi.yml)
[![check](https://github.com/MyLinuxProfile/linux-profile/actions/workflows/python-publish-pypi-test.yml/badge.svg)](https://github.com/MyLinuxProfile/linux-profile/actions/workflows/python-publish-pypi-test.yml)
[![check](https://github.com/MyLinuxProfile/linux-profile/actions/workflows/python-app-test.yml/badge.svg)](https://github.com/MyLinuxProfile/linux-profile/actions/workflows/python-app-test.yml)

---

- **Documentation**: [https://docs.linuxprofile.com](https://docs.linuxprofile.com)
- **Source Code**: [https://github.com/MyLinuxProfile/linux-profile](https://github.com/MyLinuxProfile/linux-profile)

---

# [Introduction](https://docs.linuxprofile.com/)
Linux Profile is a Linux profile management tool. With this project it is possible, from commands executed in the console, to create a 'json' file to store backup configurations. such as information about installed packages, alias. It also allows with a single command to restore saved configurations.

### Quick URLs
- Last Version -> https://linuxprofile.com/LAST_VERSION
- Install -> https://linuxprofile.com/install.sh

### Quick development URLs
- Beta -> https://linuxprofile.com/beta.sh

## [Installation](https://docs.linuxprofile.com/)

- **Install - Pypi/PIP**

      pip install -U linuxp

- **Install - Shell/Curl** - **STABLE**

      /bin/bash -c "$(curl -fsSL https://linuxprofile.com/install.sh)"

## [Wiki Page](https://docs.linuxprofile.com/)

## Commands:

| Command               | Description                                                                           | Docs                                   |
|:--------------------- |:------------------------------------------------------------------------------------- | :------------------------------------: | 
| ``linuxp config``     | Configuration of profile files and server connection.                                 | [Link](https://docs.linuxprofile.com/) |
| ``linuxp add``        | Parameter used to add a new item to the list in your profile file.                    | [Link](https://docs.linuxprofile.com/) |
| ``linuxp remove``     | Removes items from the profile file.                                                  | [Link](https://docs.linuxprofile.com/) |
| ``linuxp install``    | This parameter is used to install the modules, **package**, **alias** and **script**. | [Link](https://docs.linuxprofile.com/) |
| ``linuxp uninstall``  | Command used to uninstall items. Be **very careful** when running.                    | [Link](https://docs.linuxprofile.com/) |
| ``linuxp list``       | Lists all modules in the terminal and can also apply filters to find items.           | [Link](https://docs.linuxprofile.com/) |

## [Make a profile backup](https://docs.linuxprofile.com/)

- Saving the profile file:

      cat ~/.config/linuxp/linux_profile.json > ~/backup_profile.json

- Open in a text editor:

      xdg-open ~/backup_profile.json
        
- Open in Google Chrome browser:

      google-chrome ~/backup_profile.json
        
- Open in Firefox browser:

      firefox ~/backup_profile.json

- Open vi text editor:

      vi ~/backup_profile.json

## Profile File 

- Link - [linux_profile.json](https://linuxprofile.com/linux_profile.json)

## Commit Style
- ⚙️ NO-TASK
- 📝 PEP8
- 📌 ISSUE
- 🪲 BUG
- 📘 DOCS
- 📦 PyPI
- ❤️️ TEST

## License

This project is licensed under the terms of the MIT license.
