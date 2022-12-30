# Exemple

## Package

```bash
$> linuxp add --module package

=============== Input ===============

Package Tag [default]: music
* Package Manager: snap
* Package Name: spotify
Package URL: 
Package File: 
Package Description [limit 85]:

=============== Input ===============
```

### Package Tag

| Fixed Text  | Required | Example   | Description    |
| :---------: | :------: | :-------: |:-------------: |
|   ◻️ No      |  ◻️ No    | ``music``	| Tag group name |

### Package Manager 

| Fixed Text |   Required   | Option             | Description            |
| :--------: | :----------: | :----------------: |:---------------------: |
|   ✅ Yes   |    ✅ Yes    | ``apt-get``	     | Linux Package Manager  |
|   ✅ Yes   |    ✅ Yes    | ``apt``	         | Linux Package Manager  |
|   ✅ Yes   |    ✅ Yes    | ``snap``	         | Linux Package Manager  |
|   ✅ Yes   |    ✅ Yes    | ``yum``	         | Linux Package Manager  |
|   ✅ Yes   |    ✅ Yes    | ``dnf``	         | Linux Package Manager  |
|   ✅ Yes   |    ✅ Yes    | ``pacman``	     | Linux Package Manager  |
|   ✅ Yes   |    ✅ Yes    | ``zypper``	     | Linux Package Manager  |
|   ✅ Yes   |    ✅ Yes    | ``spack``	         | Linux Package Manager  |
|   ✅ Yes   |    ✅ Yes    | ``brew``	         | Linux Package Manager  |
|   ✅ Yes   |    ✅ Yes    | ``swupd``	         | Linux Package Manager  |
|   ✅ Yes   |    ✅ Yes    | ``guix``	         | Linux Package Manager  |
|   ✅ Yes   |    ✅ Yes    | ``flatpak``	     | Linux Package Manager  |
|   ✅ Yes   |    ✅ Yes    | ``pip``	         | Python Package Manager |

### Package Name

| Fixed Text |   Required   | Example            | Description             |
| :--------: | :----------: | :----------------: |:----------------------: |
|   ◻️ No     |    ✅ Yes    | ``spotify``  	     | Package name to install |


### Package URL

| Fixed Text  | Required | Example                     | Description    |
| :---------: | :------: | :-------------------------: |:-------------: |
|   ◻️ No      |  ◻️ No    | `https://linuxprofile.com/` |                |

### Package File

| Fixed Text  | Required | Example                | Description    |
| :---------: | :------: | :--------------------: |:-------------: |
|   ◻️ No      |  ◻️ No    | `spotify.txt`          |                |

### Package Description

| Fixed Text  | Required | Example                | Description    |
| :---------: | :------: | :--------------------: |:-------------: |
|   ◻️ No      |  ◻️ No    | `Music application`    |                |

---

## Alias

```bash
$> linuxp add --module alias

=============== Input ===============

Alias Tag [default]: music
* Alias Name: play_music
* Alias Command: play_music
* Alias Body: mplayer linuxprofile.mp3
Package Description [limit 85]: This command will play my favorite song.

=============== Input ===============
```

### Alias Tag

| Fixed Text  | Required | Example   | Description    |
| :---------: | :------: | :-------: |:-------------: |
|   ◻️ No      |  ◻️ No    | ``music``	| Tag group name |

### Alias Name

| Fixed Text | Required | Example            | Description                      |
| :--------: | :------: | :----------------: |:-------------------------------: |
|   ◻️ No     |  ✅ Yes  | ``play_music``	 | Name that references the command |

### Alias Command

| Fixed Text | Required | Example            | Description                   |
| :--------: | :------: | :----------------: |:----------------------------: |
|   ◻️ No     |  ✅ Yes  | ``play_music``	 | Command that will be executed |

### Alias Body

| Fixed Text | Required | Example                      | Description           |
| :--------: | :------: | :--------------------------: |:--------------------: |
|   ◻️ No     |  ✅ Yes  | ``mplayer linuxprofile.mp3`` | Content that will run |

### Alias Description

| Fixed Text  | Required | Example                                    | Description    |
| :---------: | :------: | :----------------------------------------: |:-------------: |
|   ◻️ No      |  ◻️ No    | `This command will play my favorite song.` |                |

---

## Script

```bash
$> linuxp add --module script

=============== Input ===============

Script Tag [default]: system
* Script Type: shell
* Script Name: clen_my_linux
* Script Body:  To finish type [end]
> sudo apt clean
> sudo apt autoclean
> sudo apt autoremove
> echo 'Cleaning Completed!'
> end
Script Shebang: 
Package Description [limit 85]: This script will clean up some memory.

=============== Input ===============
```

### Script Tag

| Fixed Text  | Required | Example       | Description    |
| :---------: | :------: | :-----------: |:-------------: |
|   ◻️ No      |  ◻️ No    | ``system``	| Tag group name |


### Script Type

| Fixed Text  | Required | Option    | Description    |
| :---------: | :------: | :-------: |:-------------: |
|   ✅ Yes    |  ✅ Yes  | `shell`	| Shell Script   |
|   ✅ Yes    |  ✅ Yes  | `python`	| Python Script  |
|   ✅ Yes    |  ✅ Yes  | `python3`	| Python Script  |
|   ✅ Yes    |  ✅ Yes  | `ruby` 	| Ruby Script    |

### Script Name

| Fixed Text  | Required | Example            | Description      |
| :---------: | :------: | :----------------: |:---------------: |
|   ◻️ No      |  ✅ Yes  | ``clen_my_linux``	 | Your script name  |

### Script Body

| Fixed Text  | Required | Example                | Description    |
| :---------: | :------: | :--------------------: |:-------------: |
|   ◻️ No      |  ✅ Yes  | `echo 'LinuxProfile!'` |                |

### Script Shebang:

| Fixed Text  | Required | Example                  | Description    |
| :---------: | :------: | :----------------------: |:-------------: |
|   ◻️ No      |  ◻️ No    | `#!/bin/bash`            | Shell Script   |
|   ◻️ No      |  ◻️ No    | `#!/usr/bin/env python`  | Python Script  |
|   ◻️ No      |  ◻️ No    | `#!/usr/bin/env python3` | Python Script  |
|   ◻️ No      |  ◻️ No    | `#!/usr/bin/env ruby`    | Ruby Script    |

### Script Description

| Fixed Text  | Required | Example                                  | Description    |
| :---------: | :------: | :--------------------------------------: |:-------------: |
|   ◻️ No      |  ◻️ No    | `This script will clean up some memory.` |                |
