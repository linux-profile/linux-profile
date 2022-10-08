import os

if os.environ.get('ENVIRONMENT') == 'DEV':
    # export ENVIRONMENT="DEV"
    PATH = os.getcwd()
else:
    PATH = f"{os.getcwd()}/linuxp"

CONFIG = '.config'
FOLDER_CONFIG = f"{PATH}/{CONFIG}"
FOLDER_PROFILE = f'{FOLDER_CONFIG}/profiles'
FOLDER_LOG = f'{FOLDER_CONFIG}/logs'

FILE = {
    "config": f'{FOLDER_CONFIG}/linux_config.json',
    "profile": f'{FOLDER_CONFIG}/linux_profile.json',
    "log_config": f"{FOLDER_LOG}/app.log",
    "log_profile": f"{FOLDER_LOG}/profile.log",
    "log_install": f"{FOLDER_LOG}/install.log",
    "distro": f'{FOLDER_CONFIG}/.os-release',
    "system": f'{FOLDER_CONFIG}/.hostnamectl',
}
