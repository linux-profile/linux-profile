from pathlib import Path

PATH = str(Path.home())

CONFIG = f"{PATH}/.config"
PATH_CONFIG = f"{CONFIG}/linuxp"
PATH_PROFILE = f'{PATH_CONFIG}/profiles'
PATH_LOG = f'{PATH_CONFIG}/logs'

folder_location = {
    "config": CONFIG,
    "config_linuxp": PATH_CONFIG,
    "profile": PATH_PROFILE,
    "log": PATH_LOG,
    "temp": "/tmp/linuxp/",
    "linuxp": "/opt/linuxp/",
}

file_location = {
    "config": f'{PATH_CONFIG}/linux_config.json',
    "profile": f'{PATH_CONFIG}/linux_profile.json',
    "log_config": f"{PATH_LOG}/app.log",
    "log_profile": f"{PATH_LOG}/profile.log",
    "log_install": f"{PATH_LOG}/install.log",
    "bash_aliases": f'{PATH}/.bash_aliases'
}
