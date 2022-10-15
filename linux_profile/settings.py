from pathlib import Path

PATH = str(Path.home())
PATH_LINUXP = f"{PATH}/linuxp"

CONFIG = '.config'
FOLDER_CONFIG = f"{PATH_LINUXP}/{CONFIG}"
FOLDER_PROFILE = f'{FOLDER_CONFIG}/profiles'
FOLDER_LOG = f'{FOLDER_CONFIG}/logs'
FOLDER_TEMP = f'{FOLDER_CONFIG}/temp'

FOLDER = {
    "linuxp": PATH_LINUXP,
    "config": FOLDER_CONFIG,
    "profile": FOLDER_PROFILE,
    "log": FOLDER_LOG,
    "temp": FOLDER_TEMP
}

FILE = {
    "config": f'{FOLDER_CONFIG}/linux_config.json',
    "profile": f'{FOLDER_CONFIG}/linux_profile.json',
    "log_config": f"{FOLDER_LOG}/app.log",
    "log_profile": f"{FOLDER_LOG}/profile.log",
    "log_install": f"{FOLDER_LOG}/install.log",
    "distro": f'{FOLDER_CONFIG}/.os-release',
    "system": f'{FOLDER_CONFIG}/.hostnamectl',
    "bash_aliases": f'{PATH}/.bash_aliases'
}
