This is a basic "how to" tutorial, showing the basic commands, manipulating a generic profile with the aim of just illustrating the general process. Then I created their own profile files, because the cool thing.

- [**Installing**](https://docs.linuxprofile.com/nav/installation/)

```bash
pip install -U linuxp
```

- [**Downloading test profile**](https://docs.linuxprofile.com/nav/commands/profile/exemple/#output)

```bash
linuxp profile --url https://linuxprofile.com/linux_profile.json --output 'my_linux.json'
```

- [**Selecting profile**](https://docs.linuxprofile.com/nav/commands/profile/exemple/#switch)

```bash
linuxp profile --switch 'my_linux.json'
```

- [**Listing existing profiles**](https://docs.linuxprofile.com/nav/commands/profile/exemple/#list)

```bash
linuxp profile --list
```

- [**Listing my packages**](https://docs.linuxprofile.com/nav/commands/list/exemple/)

```bash
linuxp list --module package
```

- [**Installing packages**](https://docs.linuxprofile.com/nav/commands/install/exemple/#install-package)

```bash
linuxp install --module package --sudo
```

- [**Package uninstall**](https://docs.linuxprofile.com/nav/commands/uninstall/exemple/#uninstall-package)

```bash
linuxp uninstall --module package --sudo
```

- [**Listing package by item name**](https://docs.linuxprofile.com/nav/commands/list/exemple/#list-item)

```bash
linuxp list --module package --item vim
```

- [**Listing package by tag name**](https://docs.linuxprofile.com/nav/commands/list/exemple/#list-tag)

```bash
linuxp list --module package --tag util
```

- [**Installation command in test mode**](https://docs.linuxprofile.com/nav/commands/install/exemple/#debug)

```bash
linuxp install --module package --item vim --debug
```

- [**Uninstallation command in test mode**](https://docs.linuxprofile.com/nav/commands/uninstall/exemple/#debug)

```bash
linuxp uninstall --module package --item vim --debug
```

- [**Installation command with admin permissions**](https://docs.linuxprofile.com/nav/commands/install/exemple/#permissions)

```bash
linuxp install --module package --item vim --sudo
```

- [**Uninstallation command with admin permissions**](https://docs.linuxprofile.com/nav/commands/uninstall/exemple/#permissions)

```bash
linuxp uninstall --module package --item vim --sudo
```

- [**List with complete data**](https://docs.linuxprofile.com/nav/commands/list/exemple/)

```bash
linuxp list --module text --print
```

- [**Single field listing**](https://docs.linuxprofile.com/nav/commands/list/exemple/)

```bash
linuxp list --module text --print --field label
```

- [**Testing script**](https://docs.linuxprofile.com/nav/commands/install/exemple/#install-script)

```bash
linuxp install -m script -i play_music
```

- [**Storing my profile file elsewhere**](https://docs.linuxprofile.com/nav/backup/)

```bash
cat ~/.config/linuxp/profile/my_linux.json > ~/backup_profile.json
```

- [**Opening file I saved elsewhere**](https://docs.linuxprofile.com/nav/backup/)

```bash
vi ~/backup_profile.json
```

