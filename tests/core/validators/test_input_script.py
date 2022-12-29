from linux_profile.validators.input_script import InputAddScript
from linux_profile.base.error import (
    ErrorOptionIsMissing,
    ErrorOptionIsInvalid,
    ErrorInvalidValue
)

types = [
    'shell',
    'python',
    'python3',
    'ruby'
]


def test_validator_input_script_tag_default():
    fields = InputAddScript(**{"tag": None})
    assert fields.tag == 'default'


def test_validator_input_script_tag_underline():
    fields = InputAddScript(**{"tag": 'linux profile'})
    assert fields.tag == 'linux_profile'


def test_validator_input_script_tag_lower():
    fields = InputAddScript(**{"tag": 'LINUXPROFILE'})
    assert fields.tag == 'linuxprofile'


def test_validator_input_script_type_option_is_missing():
    try:
        InputAddScript(**{"type": None})
    except Exception as error:
        assert error.__class__ == ErrorOptionIsMissing
        assert error.args[0] == 'Option [Script Type] is missing!'


def test_validator_input_script_type_option_is_invalid():
    try:
        InputAddScript(**{"type": "xpto"})
    except Exception as error:
        assert error.__class__ == ErrorOptionIsInvalid
        assert error.args[0] == "Option [Script Type] invalid! Usage: ['shell', 'python', 'python3', 'ruby']"


def test_validator_input_script_type_success():
    for item in types:
        fields = InputAddScript(**{"type": item})
        assert fields.type in types


def test_validator_input_script_description_success():
    fields = InputAddScript(**{"description": 'LINUX'})
    assert fields.description == 'LINUX'


def test_validator_input_script_description_default_success():
    fields = InputAddScript(**{"description": None})
    assert fields.description == 'No description'


def test_validator_input_script_description_character_limit_error():
    try:
        InputAddScript(**{"description": 42*"Linux"})
    except Exception as error:
        assert error.__class__ == ErrorInvalidValue
        assert error.args[0] == 'Option [Script Description] invalid value!'
