from linux_profile.validators.input_package import InputAddPackage
from linux_profile.base.error import (
    ErrorOptionIsMissing,
    ErrorOptionIsInvalid,
    ErrorInvalidValue
)

types = [
    'apt-get',
    'apt',
    'snap',
    'yum',
    'dnf',
    'pacman',
    'zypper',
    'spack',
    'brew',
    'pip',
    'swupd',
    'guix',
    'flatpak'
]


def test_validator_input_package_tag_default():
    fields = InputAddPackage(**{"tag": None})
    assert fields.tag == 'default'


def test_validator_input_package_tag_underline():
    fields = InputAddPackage(**{"tag": 'linux profile'})
    assert fields.tag == 'linux_profile'


def test_validator_input_package_tag_lower():
    fields = InputAddPackage(**{"tag": 'LINUXPROFILE'})
    assert fields.tag == 'linuxprofile'


def test_validator_input_package_type_option_is_missing():
    try:
        InputAddPackage(**{"type": None})
    except Exception as error:
        assert error.__class__ == ErrorOptionIsMissing
        assert error.args[0] == 'Option [Package Manager] is missing!'


def test_validator_input_package_type_option_is_invalid():
    try:
        InputAddPackage(**{"type": "xpto"})
    except Exception as error:
        assert error.__class__ == ErrorOptionIsInvalid


def test_validator_input_package_type_success():
    for item in types:
        fields = InputAddPackage(**{"type": item})
        assert fields.type in types


def test_validator_input_package_name_success():
    fields = InputAddPackage(**{"name": '\tLINUX\u001b[C'})
    assert fields.name == 'LINUX'


def test_validator_input_package_name_error():
    try:
        InputAddPackage(**{"name": None})
    except Exception as error:
        assert error.__class__ == ErrorOptionIsMissing
        assert error.args[0] == 'Option [Package Name] is missing!'


def test_validator_input_package_description_success():
    fields = InputAddPackage(**{"description": '\tLINUX\u001b[C'})
    assert fields.description == 'LINUX'


def test_validator_input_package_description_default_success():
    fields = InputAddPackage(**{"description": None})
    assert fields.description == 'No description'


def test_validator_input_package_description_character_limit_error():
    try:
        InputAddPackage(**{"description": 42*"Linux"})
    except Exception as error:
        assert error.__class__ == ErrorInvalidValue
        assert error.args[0] == 'Option [Package Description] invalid value!'


def test_validator_input_package_generate_all_success():
    names = "linuxp,linuxprofile,linux"
    fields = InputAddPackage(**{
            "tag": None,
            "name": names,
            "type": "pacman",
            "url": None,
            "file": None,
            "description": None
        }
    )
    content = fields.generate_all()
    assert len(content) == 3
    for item in content:
        assert item.get("name") in names.split(",")
