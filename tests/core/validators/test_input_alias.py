from linux_profile.validators.input_alias import InputAddAlias
from linux_profile.base.error import (
    ErrorOptionIsMissing,
    ErrorInvalidValue
)


def test_validator_input_alias_tag_default():
    fields = InputAddAlias(**{"tag": None})
    assert fields.tag == 'default'


def test_validator_input_alias_tag_underline():
    fields = InputAddAlias(**{"tag": 'linux profile'})
    assert fields.tag == 'linux_profile'


def test_validator_input_alias_tag_lower():
    fields = InputAddAlias(**{"tag": 'LINUXPROFILE'})
    assert fields.tag == 'linuxprofile'


def test_validator_input_alias_name_success():
    fields = InputAddAlias(**{"name": 'LINUX'})
    assert fields.name == 'linux'


def test_validator_input_alias_name_error():
    try:
        InputAddAlias(**{"name": None})
    except Exception as error:
        assert error.__class__ == ErrorOptionIsMissing
        assert error.args[0] == 'Option [Alias Name] is missing!'


def test_validator_input_alias_body_success():
    fields = InputAddAlias(**{"body": 'LINUX'})
    assert fields.body == 'LINUX'


def test_validator_input_alias_body_error():
    try:
        InputAddAlias(**{"body": None})
    except Exception as error:
        assert error.__class__ == ErrorOptionIsMissing
        assert error.args[0] == 'Option [Alias Body] is missing!'


def test_validator_input_alias_description_success():
    fields = InputAddAlias(**{"description": '\tLINUX\u001b[C'})
    assert fields.description == 'LINUX'


def test_validator_input_alias_description_success():
    fields = InputAddAlias(**{"description": 'LINUX'})
    assert fields.description == 'LINUX'


def test_validator_input_alias_description_default_success():
    fields = InputAddAlias(**{"description": None})
    assert fields.description == 'No description'


def test_validator_input_alias_description_character_limit_error():
    try:
        InputAddAlias(**{"description": 42*"Linux"})
    except Exception as error:
        assert error.__class__ == ErrorInvalidValue
        assert error.args[0] == 'Option [Alias Description] invalid value!'
