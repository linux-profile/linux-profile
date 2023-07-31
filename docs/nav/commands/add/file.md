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


=== "File Path"

    | Fixed Text  | Required | Example         | Description    |
    | :---------: | :------: | :-------------: |:-------------: |
    |   ◻️ No      |  ✅ Yes  | `~/LICENCE/`    |                |

=== "Body"

    | Fixed Text  | Required | Example                                                | Description    |
    | :---------: | :------: | :----------------------------------------------------: |:-------------: |
    |   ◻️ No      |  ◻️ No    | `MIT License\n\nCopyright (c) 2023 Linux Profile\n...` |                |
