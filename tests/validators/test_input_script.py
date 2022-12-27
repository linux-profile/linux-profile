from linux_profile.validators.input_script import InputAddScript
from linux_profile.base.error import (
    ErrorOptionIsMissing,
    ErrorOptionIsInvalid
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


def test_validator_input_script_type_option_is_invalid():
    try:
        InputAddScript(**{"type": "xpto"})
    except Exception as error:
        assert error.__class__ == ErrorOptionIsInvalid


def test_validator_input_script_type_success():
    for item in types:
        fields = InputAddScript(**{"type": item})
        assert fields.type in types
