from linux_profile.validators.input_config import InputConfig
from linux_profile.base.error import (
    ErrorArgumentIsInvalid,
    ErrorOptionIsMissing
)


def test_validator_input_config_url_success():
    url = 'https://linuxprofile.com/linux_config.json'
    fields = InputConfig(**{"url": url})
    assert fields.url == url


def test_validator_input_config_url_error():
    try:
        InputConfig(**{"url": 'linuxprofile.com/linux_config.json'})
    except ErrorArgumentIsInvalid as error:
        error.__class__ == ErrorArgumentIsInvalid
        assert str(error) == 'Argument [--url] invalid! The URL must have http or https.'


def test_validator_input_config_editor_sucess():
    editor = "vim"
    fields = InputConfig(**{"editor": editor})
    assert fields.editor == editor


def test_validator_input_config_editor_error():
    try:
        InputConfig(**{"editor": None})
    except ErrorOptionIsMissing as error:
        error.__class__ == ErrorOptionIsMissing
        assert str(error) == 'Option [Editor Name] is missing!'
