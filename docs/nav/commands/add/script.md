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

=== "Shebang"

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
