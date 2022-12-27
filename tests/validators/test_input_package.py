from linux_profile.validators.input_package import InputAddPackage
from linux_profile.base.error import (
    ErrorOptionIsMissing,
    ErrorOptionIsInvalid
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
    'shell',
    'deb'
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


def test_validator_input_package_type_option_is_invalid():
    try:
        InputAddPackage(**{"type": "xpto"})
    except Exception as error:
        assert error.__class__ == ErrorOptionIsInvalid


def test_validator_input_package_type_success():
    for item in types:
        fields = InputAddPackage(**{"type": item})
        assert fields.type in types
