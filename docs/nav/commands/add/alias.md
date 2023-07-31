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
