from pathlib import Path

PATH = str(Path.home())

PATH_CONFIG = f"{PATH}/.config"
PATH_LINUXP = f"{PATH_CONFIG}/linuxp"
PATH_PROFILE = f'{PATH_LINUXP}/profiles'
PATH_LOG = f'{PATH_LINUXP}/logs'

folder_location = {
    "config": PATH_CONFIG,
    "linuxp": PATH_LINUXP,
    "profile": PATH_PROFILE,
    "log": PATH_LOG,
    "temp": "/tmp/linuxp"
}

file_location = {
    "config": f'{PATH_LINUXP}/linux_config.json',
    "profile": f'{PATH_LINUXP}/linux_profile.json',
    "log_app": f"{PATH_LOG}/app.log",
    "bash_aliases": f'{PATH}/.bash_aliases'
}
