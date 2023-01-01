from linux_profile.validators.input_file import InputAddFile
from linux_profile.base.error import (
    ErrorOptionIsMissing,
    ErrorOptionIsInvalid
)

types = [
    "create",
    "read",
    "update",
    "delete"
]


def test_validator_input_file_tag_default():
    fields = InputAddFile(**{"tag": None})
    assert fields.tag == "default"


def test_validator_input_file_tag_underline():
    fields = InputAddFile(**{"tag": "linux profile"})
    assert fields.tag == "linux_profile"


def test_validator_input_file_type_option_is_missing():
    try:
        InputAddFile(**{"type": None})
    except Exception as error:
        assert error.__class__ == ErrorOptionIsMissing
        assert error.args[0] == "Option [File Operation Type ] is missing!"


def test_validator_input_file_type_option_is_invalid():
    try:
        InputAddFile(**{"type": "xpto"})
    except Exception as error:
        assert error.__class__ == ErrorOptionIsInvalid
        assert error.args[0] == "Option [File Operation Type ] invalid! Usage: ['create', 'read', 'update', 'delete']"


def test_validator_input_file_type_success():
    for item in types:
        fields = InputAddFile(**{"type": item})
        assert fields.type in types
