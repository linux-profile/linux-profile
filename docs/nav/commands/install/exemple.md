# Exemple

## Permissions

Run the installation commands with administrator permission.

- Input

```bash
linuxp install --module package --sudo on
```

- Command result

```bash
sudo apt install python3
sudo apt install python3-pip
```

## Debug

Run the installation commands in test mode. In test mode the commands are not
actually executed on the machine, they are just displayed in the terminal.

- Input

```bash
linuxp install --module package --debug on
```

- Command result

```bash
echo 'sudo apt install python3'
echo 'sudo apt install python3-pip'
```

## Group

This command groups the items for executing the command.

- Input

```bash
linuxp install --module package --group on
```

- Command result

```bash
sudo apt install python3 python3-pip
```

## Install Package


### Module

**Full Command**
```bash
linuxp install --module package
```
**Short Command**
```bash
linuxp install -m package
```

### Tag

**Full Command**
```bash
linuxp install --module package --tag music
```
**Short Command**
```bash
linuxp install -m package -t music
```

### Item

**Full Command**
```bash
linuxp install --module package --tag music --item spotify
```

**Short Command**
```bash
linuxp install -m package -t music -i spotify
```

## Install Script

### Module

**Full Command**
```bash
linuxp install --module script
```
**Short Command**
```bash
linuxp install -m script
```

### Tag

**Full Command**
```bash
linuxp install --module script --tag system
```
**Short Command**
```bash
linuxp install -m script -t system
```

### Item

**Full Command**
```bash
linuxp install --module script --tag system --item clean_my_linux
```

**Short Command**
```bash
linuxp install -m script -t system -i clean_my_linux
```


## Install Alias

### Module

**Full Command**
```bash
linuxp install --module alias
```
**Short Command**
```bash
linuxp install -m alias
```

### Tag

**Full Command**
```bash
linuxp install --module alias --tag music
```
**Short Command**
```bash
linuxp install -m alias -t music
```

### Item

**Full Command**
```bash
linuxp install --module alias --tag music --item play_music
```

**Short Command**
```bash
linuxp install -m alias -t music -i play_music
```