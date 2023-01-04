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

Package Tag [default]: music
* Package Manager: snap
* Package Name: spotify
Package URL: 
Package File: 
Package Description [limit 85]:

=============== Input ===============
```

### Fields

=== "Tag"

    | Fixed Text  | Required | Example   | Description    |
    | :---------: | :------: | :-------: |:-------------: |
    |   ◻️ No      |  ◻️ No    | ``music``	| Tag group name |

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
    |   ◻️ No     |    ✅ Yes    | ``spotify``  	     | Package name to install |


=== "Package URL"

    | Fixed Text  | Required | Example                     | Description    |
    | :---------: | :------: | :-------------------------: |:-------------: |
    |   ◻️ No      |  ◻️ No    | `https://linuxprofile.com/` |                |

=== "File"

    | Fixed Text  | Required | Example                | Description    |
    | :---------: | :------: | :--------------------: |:-------------: |
    |   ◻️ No      |  ◻️ No    | `spotify.txt`          |                |


=== "Description"

    | Fixed Text  | Required | Example                | Description    |
    | :---------: | :------: | :--------------------: |:-------------: |
    |   ◻️ No      |  ◻️ No    | `Music application`    |                |

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

Alias Tag [default]: music
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
    |   ◻️ No      |  ◻️ No    | ``music``	| Tag group name |

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
