# Welcome to LinuxProfile

<img src="https://github.com/MyLinuxProfile/linux-profile/blob/master/docs/linuxp.png?raw=true">

![GitHub Org's stars](https://img.shields.io/github/stars/MyLinuxProfile?label=LinuxProfile&style=flat-square)
![GitHub last commit](https://img.shields.io/github/last-commit/MyLinuxProfile/linux-profile-basic?style=flat-square)
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

**English**: Linux Profile is a CLI tool for Linux profile management. With this project it is possible, from commands executed in the console, to create a 'json' file to store the backup configurations. For example, information about packages, aliases, scripts, texts and files. It also allows with a single command to restore the saved settings.

> **Português**: Linux Profile é uma ferramenta de CLI para gerenciamento de perfil do Linux. Com este projeto é possível, a partir de comandos executados no console, criar um arquivo 'json' para armazenar as configurações de backup. Como por exemplo,  informações sobre pacotes, alias, scripts, textos e arquivos. Também permite com um único comando restaurar as configurações salvas.

# [How and why?](https://docs.linuxprofile.com/)

**English**: With the need to automate processes and execution of scripts, **LinuxProfile** emerged, a project developed in python that aims to create a standard in the chaos of storing information about scripts, aliases, packages, texts and files in a single place, fully customizable from according to the user.

> **Português**: Com a necessidade de automatizar os processos e execução de scripts, surgiu **LinuxProfile**, projeto desenvolvido em python que tem como objetivo criar um padrão no caos do armazenamento de informações de scripts, alias, packages, textos e arquivos em um único local, totalmente personalizável de acordo com o usuário.

### Quick URLs
- Last Version -> https://linuxprofile.com/LAST_VERSION
- Install -> https://linuxprofile.com/install.sh

### Quick development URLs
- Beta -> https://linuxprofile.com/beta.sh

## Commands

| Command               | Description                                                                           | Docs                                   |
|:--------------------- |:------------------------------------------------------------------------------------- | :------------------------------------: | 
| ``linuxp config``     | Settings file management.                                                             | [Link](/nav/commands/config/) |
| ``linuxp profile``    | Profile file management.                                                              | [Link](/nav/commands/profile/) |
| ``linuxp add``        | Parameter used to add a new item to the list in your profile file.                    | [Link](/nav/commands/add/) |
| ``linuxp remove``     | Removes items from the profile file.                                                  | [Link](/nav/commands/remove/) |
| ``linuxp install``    | This parameter is used to install the modules, **package**, **alias** and **script**. | [Link](/nav/commands/install/) |
| ``linuxp uninstall``  | Command used to uninstall items. Be **very careful** when running.                    | [Link](/nav/commands/uninstall/) |
| ``linuxp list``       | Lists all modules in the terminal and can also apply filters to find items.           | [Link](/nav/commands/list/) |

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
