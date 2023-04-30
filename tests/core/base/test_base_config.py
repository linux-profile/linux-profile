from os import getcwd
from pathlib import Path
from shutil import rmtree
from linux_profile.base.settings import Settings


def path(value: str) -> str:
    return Path(getcwd()).joinpath("tests/helpers/" + value)


class ConfigTest(Settings):

    attr_base = []
    attr_variable = []

    class Base:
        path_install = path("/opt/linuxp")
        path_temp = path("/tmp/linuxp")
        path_config = path(".config/linuxp")
        path_profile = path(".config/linuxp/profile")
        file_aliases = path(".bash_aliases")
        file_bashrc = path(".bashrc")
        file_config = "linux_config.json"

    class Variable:
        file_profile = "linux_profile.json"
        text_editor = "vim"

    def __init__(self, **kwargs) -> None:
        self.profile = {}
        self.config = {}

        for arg in kwargs:
            setattr(self, arg, kwargs.get(arg))

        self._load_attributes()
        self.setup()


def test_base_config_load_base():
    home = getcwd()
    config = ConfigTest()
    attributes = [
        'path_install',
        'path_temp',
        'path_config',
        'path_profile',
        'file_aliases',
        'file_bashrc',
        'file_config',
        'file_profile',
        'text_editor'
    ]

    assert config.profile == {}
    assert config.config == {}

    assert str(config.path_install) == f"{home}/tests/helpers/opt/linuxp"
    assert str(config.path_temp) == f"{home}/tests/helpers/tmp/linuxp"
    assert str(config.path_config) == f"{home}/tests/helpers/.config/linuxp"
    assert str(config.file_aliases) == f"{home}/tests/helpers/.bash_aliases"
    assert str(config.file_bashrc) == f"{home}/tests/helpers/.bashrc"
    assert str(config.file_profile) == "linux_profile.json"
    assert str(config.file_config) == "linux_config.json"
    assert str(config.text_editor) == "vim"

    assert config.attr_base + config.attr_variable == attributes


def test_base_config_load_path():
    home = getcwd()
    config = ConfigTest()
    config._load_structure()

    assert config.path_profile.exists() == True
    assert config.path_config.exists() == True
    assert config.path_install.exists() == True
    assert config.path_temp.exists() == True

    rmtree(f"{home}/tests/helpers/opt")
    rmtree(f"{home}/tests/helpers/.config")
    rmtree(f"{home}/tests/helpers/tmp/")
