from shutil import rmtree
from os import getcwd, path
from linux_profile.base.settings import Settings


PATH = getcwd()


def config_path(value: str) -> str:
    home = f"{PATH}/tests/helpers"
    return "/".join([home, value])


class ConfigTest(Settings):

    attributes = []

    class Base:
        path_install = config_path("opt/linuxp")
        path_temp = config_path("tmp/linuxp")
        path_config = config_path(".config/linuxp")
        file_aliases = config_path(".bash_aliases")
        file_bashrc = config_path(".bashrc")
        file_profile = "linux_profile.json"
        file_config = "linux_config.json"

    def __init__(self, **kwargs) -> None:
        self.profile = {}
        self.config = {}

        for arg in kwargs:
            setattr(self, arg, kwargs.get(arg))

        self._load_attributes()
        self.setup()


def test_base_config_load_attributes():
    config = ConfigTest()
    attributes = [
        'path_install',
        'path_temp',
        'path_config',
        'file_aliases',
        'file_bashrc',
        'file_profile',
        'file_config'
    ]

    assert config.profile ==  {}
    assert config.config ==  {}

    assert config.path_install == f"{PATH}/tests/helpers/opt/linuxp"
    assert config.path_temp == f"{PATH}/tests/helpers/tmp/linuxp"
    assert config.path_config == f"{PATH}/tests/helpers/.config/linuxp"
    assert config.file_aliases == f"{PATH}/tests/helpers/.bash_aliases"
    assert config.file_bashrc == f"{PATH}/tests/helpers/.bashrc"
    assert config.file_profile == "linux_profile.json"
    assert config.file_config == "linux_config.json"

    assert config.attributes == attributes


def test_base_config_load_structure():
    config = ConfigTest()
    config._load_structure()

    assert path.exists(config.path_install) == True
    assert path.exists(config.path_temp) == True
    assert path.exists(config.path_config) == True

    rmtree(f"{PATH}/tests/helpers/opt")
    rmtree(f"{PATH}/tests/helpers/.config")
    rmtree(f"{PATH}/tests/helpers/tmp/")
