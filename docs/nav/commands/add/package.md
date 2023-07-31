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
* Package Manager: pacman
* Package Name: vim
Package Version:
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
    |   ✅ Yes   |    ✅ Yes    | ``poetry``	     | Python Package Manager  |
    |   ✅ Yes   |    ✅ Yes    | ``conda``	     | Python Package Manager  |
    |   ✅ Yes   |    ✅ Yes    | ``gem``	     | Ruby Package Manager  |
    |   ✅ Yes   |    ✅ Yes    | ``npm``	     | Node.js and JavaScript Package Manager  |
    |   ✅ Yes   |    ✅ Yes    | ``yarn``	     | Node.js and JavaScript Package Manager  |
    |   ✅ Yes   |    ✅ Yes    | ``port``	     | MacOS Package Manager  |
    |   ✅ Yes   |    ✅ Yes    | ``fink``	     | MacOS Package Manager  |

=== "Name"

    | Fixed Text |   Required   | Example            | Description             |
    | :--------: | :----------: | :----------------: |:----------------------: |
    |   ◻️ No     |    ✅ Yes    | ``vim``  	     | Package name to install |

=== "Version"

    | Fixed Text |   Required   | Example            | Description             |
    | :--------: | :----------: | :----------------: |:----------------------: |
    |   ◻️ No     |    ◻️ No      | ``1.0.0``   	   | Works with ``PIP`` only |

=== "URL"

    | Fixed Text  | Required | Example                     | Description    |
    | :---------: | :------: | :-------------------------: |:-------------: |
    |   ◻️ No      |  ◻️ No    | `https://linuxprofile.com/` |                |

=== "File"

    | Fixed Text  | Required | Example                | Description    |
    | :---------: | :------: | :--------------------: |:-------------: |
    |   ◻️ No      |  ◻️ No    | `vim.txt`              |                |


=== "Description"

    | Fixed Text  | Required | Example                | Description    |
    | :---------: | :------: | :--------------------: |:-------------: |
    |   ◻️ No      |  ◻️ No    | `Text application`     |                |
