# Exemple

## Package


 - **Full Command**

```bash
linuxp add --module package
```

- **Short Command**

```bash
linuxp add -m package
```

### Input

```bash
=============== Input ===============

Package Tag [default]: util
* Package Manager: snap
* Package Name: vim
Package URL: 
Package File: 
Package Description [limit 85]:

=============== Input ===============
```

### Fields

=== "Tag"

    | Fixed Text  | Required | Example   | Description    |
    | :---------: | :------: | :-------: |:-------------: |
    |   ◻️ No      |  ◻️ No    | ``util``	| Tag group name |

=== "Manager"

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

=== "Name"

    | Fixed Text |   Required   | Example            | Description             |
    | :--------: | :----------: | :----------------: |:----------------------: |
    |   ◻️ No     |    ✅ Yes    | ``vim``  	     | Package name to install |


=== "Package URL"

    | Fixed Text  | Required | Example                     | Description    |
    | :---------: | :------: | :-------------------------: |:-------------: |
    |   ◻️ No      |  ◻️ No    | `https://linuxprofile.com/` |                |

=== "File"

    | Fixed Text  | Required | Example                | Description    |
    | :---------: | :------: | :--------------------: |:-------------: |
    |   ◻️ No      |  ◻️ No    | `vim.txt`          |                |


=== "Description"

    | Fixed Text  | Required | Example                | Description    |
    | :---------: | :------: | :--------------------: |:-------------: |
    |   ◻️ No      |  ◻️ No    | `Text application`    |                |

## Alias

- **Full Command**

```bash
linuxp add --module alias
```

- **Short Command**

```bash
linuxp add -m alias
```

### Input

```bash
=============== Input ===============

Alias Tag [default]: util
* Alias Name: play_music
* Alias Command: play_music
* Alias Body: mplayer linuxprofile.mp3
Package Description [limit 85]: This command will play my favorite song.

=============== Input ===============
```

### Fields

=== "Tag"

    | Fixed Text  | Required | Example   | Description    |
    | :---------: | :------: | :-------: |:-------------: |
    |   ◻️ No      |  ◻️ No    | ``util``	| Tag group name |

=== "Name"

    | Fixed Text | Required | Example            | Description                      |
    | :--------: | :------: | :----------------: |:-------------------------------: |
    |   ◻️ No     |  ✅ Yes  | ``play_music``	 | Name that references the command |

=== "Command"

    | Fixed Text | Required | Example            | Description                   |
    | :--------: | :------: | :----------------: |:----------------------------: |
    |   ◻️ No     |  ✅ Yes  | ``play_music``	 | Command that will be executed |

=== "Body"

    | Fixed Text | Required | Example                      | Description           |
    | :--------: | :------: | :--------------------------: |:--------------------: |
    |   ◻️ No     |  ✅ Yes  | ``mplayer linuxprofile.mp3`` | Content that will run |

=== "Description"

    | Fixed Text  | Required | Example                                    | Description    |
    | :---------: | :------: | :----------------------------------------: |:-------------: |
    |   ◻️ No      |  ◻️ No    | `This command will play my favorite song.` |                |

## Script

- **Full Command**

```bash
linuxp add --module script
```

- **Short Command**

```bash
linuxp add -m script
```

### Input

```bash
=============== Input ===============

Script Tag [default]: system
* Script Type: shell
* Script Name: clean_my_linux
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

### Fields

=== "Tag"

    | Fixed Text  | Required | Example       | Description    |
    | :---------: | :------: | :-----------: |:-------------: |
    |   ◻️ No      |  ◻️ No    | ``system``	| Tag group name |

=== "Type"

    | Fixed Text  | Required | Option    | Description    |
    | :---------: | :------: | :-------: |:-------------: |
    |   ✅ Yes    |  ✅ Yes  | `shell`	| Shell Script   |
    |   ✅ Yes    |  ✅ Yes  | `python`	| Python Script  |
    |   ✅ Yes    |  ✅ Yes  | `python3`	| Python Script  |
    |   ✅ Yes    |  ✅ Yes  | `ruby` 	| Ruby Script    |

=== "Name"

    | Fixed Text  | Required | Example            | Description      |
    | :---------: | :------: | :----------------: |:---------------: |
    |   ◻️ No      |  ✅ Yes  | ``clean_my_linux``	 | Your script name  |

=== "Body"

    | Fixed Text  | Required | Example                | Description    |
    | :---------: | :------: | :--------------------: |:-------------: |
    |   ◻️ No      |  ✅ Yes  | `echo 'LinuxProfile!'` |                |

=== "Shebang:"

    | Fixed Text  | Required | Example                  | Description    |
    | :---------: | :------: | :----------------------: |:-------------: |
    |   ◻️ No      |  ◻️ No    | `#!/bin/bash`            | Shell Script   |
    |   ◻️ No      |  ◻️ No    | `#!/usr/bin/env python`  | Python Script  |
    |   ◻️ No      |  ◻️ No    | `#!/usr/bin/env python3` | Python Script  |
    |   ◻️ No      |  ◻️ No    | `#!/usr/bin/env ruby`    | Ruby Script    |

=== "Description"

    | Fixed Text  | Required | Example                                  | Description    |
    | :---------: | :------: | :--------------------------------------: |:-------------: |
    |   ◻️ No      |  ◻️ No    | `This script will clean up some memory.` |                |


## Text

- **Full Command**

```bash
linuxp add --module text
```

- **Short Command**

```bash
linuxp add -m text
```

### Input

```bash
=============== Input ===============

Tag [default]: urls
* Name: linux_profile
* Text: https://docs.linuxprofile.com/
Label: linux,shell,python,dev,tech

=============== Input ===============
```

### Fields

=== "Tag"

    | Fixed Text  | Required | Example       | Description    |
    | :---------: | :------: | :-----------: |:-------------: |
    |   ◻️ No      |  ◻️ No    | ``urls``	   | Tag group name |

=== "Name"

    | Fixed Text  | Required | Example            | Description      |
    | :---------: | :------: | :----------------: |:---------------: |
    |   ◻️ No      |  ✅ Yes  | ``linux_profile``  | Your text name   |


=== "Text"

    | Fixed Text  | Required | Example                             | Description    |
    | :---------: | :------: | :---------------------------------: |:-------------: |
    |   ◻️ No      |  ✅ Yes  | `https://docs.linuxprofile.com/`    |                |

=== "Label"

    | Fixed Text  | Required | Example                          | Description    |
    | :---------: | :------: | :------------------------------: |:-------------: |
    |   ◻️ No      |  ◻️ No    | `linux,shell,python,dev,tech`    |                |


## File

- **Full Command**

```bash
linuxp add --module file
```

- **Short Command**

```bash
linuxp add -m file
```

### Input

```bash
=============== Input ===============

File Tag [default]: configs
* File Name: licence
* File Path: ~/LICENCE/
Enter text editor [vim]: vim

=============== Input ===============
```

### Fields

=== "Tag"

    | Fixed Text  | Required | Example       | Description    |
    | :---------: | :------: | :-----------: |:-------------: |
    |   ◻️ No      |  ◻️ No    | ``configs``   | Tag group name |

=== "Name"

    | Fixed Text  | Required | Example       | Description      |
    | :---------: | :------: | :-----------: |:---------------: |
    |   ◻️ No      |  ✅ Yes  | ``licence``   | Your text name   |


=== "file_path"

    | Fixed Text  | Required | Example         | Description    |
    | :---------: | :------: | :-------------: |:-------------: |
    |   ◻️ No      |  ✅ Yes  | `~/LICENCE/`    |                |

=== "body"

    | Fixed Text  | Required | Example                                                | Description    |
    | :---------: | :------: | :----------------------------------------------------: |:-------------: |
    |   ◻️ No      |  ◻️ No    | `MIT License\n\nCopyright (c) 2023 Linux Profile\n...` |                |