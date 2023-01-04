from shutil import rmtree
from os import getcwd, path
from linux_profile.base.config import Config


PATH = getcwd()

class ConfigTest(Config):

    attributes = []

    class Meta:
        linuxp_path = f"{PATH}/tests/helpers/opt/linuxp"
        linuxp_path_config = f"{PATH}/tests/helpers/.config/linuxp"
        linuxp_path_temp = f"{PATH}/tests/helpers/tmp/linuxp"
        linuxp_file_profile = "linux_profile.json"
        linuxp_file_config = "linux_profile.conf"

    def __init__(self, **kwargs) -> None:
        self.profile = None
        self.config = None

        for arg in kwargs:
            setattr(self, arg, kwargs.get(arg))

        self._load_attributes()
        self.setup()


def test_base_config_load_attributes():
    config = ConfigTest()
    attributes = [
        'linuxp_path',
        'linuxp_path_config',
        'linuxp_path_temp',
        'linuxp_file_profile',
        'linuxp_file_config'
    ]

    assert config.profile ==  None
    assert config.config ==  None

    assert config.linuxp_path == f"{PATH}/tests/helpers/opt/linuxp"
    assert config.linuxp_path_config == f"{PATH}/tests/helpers/.config/linuxp"
    assert config.linuxp_path_temp == f"{PATH}/tests/helpers/tmp/linuxp"
    assert config.linuxp_file_profile == "linux_profile.json"
    assert config.linuxp_file_config == "linux_profile.conf"

    assert config.attributes == attributes


def test_base_config_load_structure():
    config = ConfigTest()
    config._load_structure()

    assert path.exists(config.linuxp_path) == True
    assert path.exists(config.linuxp_path_config) == True
    assert path.exists(config.linuxp_path_temp) == True

    rmtree(f"{PATH}/tests/helpers/opt")
    rmtree(f"{PATH}/tests/helpers/.config")
    rmtree(f"{PATH}/tests/helpers/tmp/")
