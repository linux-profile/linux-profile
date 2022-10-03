import os

if os.environ.get('ENVIRONMENT') == 'DEV':
    # export ENVIRONMENT="DEV"
    PATH = os.getcwd()
else:
    PATH = f"{os.getcwd()}/linuxp"

CONFIG = '.config'

FOLDER_CONFIG = f"{PATH}/{CONFIG}"
FOLDER_PROFILE = f'{FOLDER_CONFIG}/profiles'
FOLDER_MODULE = f'{FOLDER_CONFIG}/modules'
FOLDER_LOG = f'{FOLDER_CONFIG}/logs'

FILE_CONFIG = f'{FOLDER_CONFIG}/linux_config.json'
FILE_PROFILE = f'{FOLDER_CONFIG}/linux_profile.json'

FILE_CONFIG_LOG = f"{FOLDER_LOG}/app.log"
FILE_PROFILE_LOG = f"{FOLDER_LOG}/profile.log"
FILE_INSTALL_LOG = f"{FOLDER_LOG}/install.log"

FILE_DISTRO = f'{FOLDER_CONFIG}/.os-release'
FILE_SYSTEM = f'{FOLDER_CONFIG}/.hostnamectl'
