# Exemple

## Permissions

Run the installation commands with administrator permission.
```bash
linuxp uninstall --module package --sudo on
```

## Debug

Run the installation commands in test mode. In test mode the commands are not
actually executed on the machine, they are just displayed in the terminal.

```bash
linuxp uninstall --module package --debug on
```


## Uninstall Package

### Module

**Full Command**
```bash
linuxp uninstall --module package
```
**Short Command**
```bash
linuxp uninstall -m package
```

### Tag

**Full Command**
```bash
linuxp uninstall --module package --tag music
```
**Short Command**
```bash
linuxp uninstall -m package -t music
```

### Item

**Full Command**
```bash
linuxp uninstall --module package --tag music --item spotify
```

**Short Command**
```bash
linuxp uninstall -m package -t music -i spotify
```

## Uninstall Script

### Module

**Full Command**
```bash
linuxp uninstall --module script
```
**Short Command**
```bash
linuxp uninstall -m script
```

### Tag

**Full Command**
```bash
linuxp uninstall --module script --tag system
```
**Short Command**
```bash
linuxp uninstall -m script -t system
```

### Item

**Full Command**
```bash
linuxp uninstall --module script --tag system --item clean_my_linux
```

**Short Command**
```bash
linuxp uninstall -m script -t system -i clean_my_linux
```


## Uninstall Alias

### Module

**Full Command**
```bash
linuxp uninstall --module alias
```
**Short Command**
```bash
linuxp uninstall -m alias
```

### Tag

**Full Command**
```bash
linuxp uninstall --module alias --tag music
```
**Short Command**
```bash
linuxp uninstall -m alias -t music
```

### Item

**Full Command**
```bash
linuxp uninstall --module alias --tag music --item play_music
```

**Short Command**
```bash
linuxp uninstall -m alias -t music -i play_music
```