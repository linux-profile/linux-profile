from os import makedirs

from linux_profile.base.settings import Settings
from linux_profile.validators.input_profile import InputProfile
from linux_profile.base.error import ErrorArgumentIsInvalid


def test_validator_input_profile_url_success():
    url = 'https://linuxprofile.com/linux_profile.json'
    fields = InputProfile(**{"url": url})
    assert fields.url == url


def test_validator_input_profile_url_error():
    try:
        InputProfile(**{"url": 'linuxprofile.com/linux_profile.json'})
    except ErrorArgumentIsInvalid as error:
        error.__class__ == ErrorArgumentIsInvalid
        assert str(error) == 'Argument [--url] invalid! The URL must have http or https.'


def test_validator_input_profile_switch_success():
    switch_file = 'switch.json'

    if not Settings.Base.path_profile.exists():
        makedirs(str(Settings.Base.path_profile))
    Settings.Base.path_profile.joinpath(switch_file).touch()

    fields = InputProfile(**{"switch": switch_file})
    assert fields.switch == switch_file

    Settings.Base.path_profile.joinpath(switch_file).unlink()


def test_validator_input_profile_switch_error():
    try:
        InputProfile(**{"switch": 'switch.json'})
    except ErrorArgumentIsInvalid as error:
        error.__class__ == ErrorArgumentIsInvalid
        assert str(error) == 'Argument [--switch] invalid! Profile file does not exist.'


def test_validator_input_profile_output_success():
    output_file = 'output.json'
    fields = InputProfile(**{"output": output_file})
    assert fields.output == str(Settings.Base.path_profile.joinpath(output_file))


def test_validator_input_profile_output_json_extension_error():
    try:
        InputProfile(**{"output": 'switch.txt'})
    except ErrorArgumentIsInvalid as error:
        error.__class__ == ErrorArgumentIsInvalid
        assert str(error) == 'Argument [--output] invalid! File name is invalid. It is necessary to put the .json extension.'


def test_validator_input_profile_output_json_characters_error():
    try:
        InputProfile(**{"output": '.json'})
    except ErrorArgumentIsInvalid as error:
        error.__class__ == ErrorArgumentIsInvalid
        assert str(error) == 'Argument [--output] invalid! File name is invalid. Must be more than five (5) characters.'


def test_validator_input_profile_new_success():
    new_file = 'new.json'
    fields = InputProfile(**{"new": new_file})
    assert fields.new == Settings.Base.path_profile.joinpath(new_file)


def test_validator_input_profile_new_json_extension_error():
    try:
        InputProfile(**{"new": 'new.txt'})
    except ErrorArgumentIsInvalid as error:
        error.__class__ == ErrorArgumentIsInvalid
        assert str(error) == 'Argument [--new] invalid! File name is invalid. It is necessary to put the .json extension.'


def test_validator_input_profile_new_json_characters_error():
    try:
        InputProfile(**{"new": '.json'})
    except ErrorArgumentIsInvalid as error:
        error.__class__ == ErrorArgumentIsInvalid
        assert str(error) == 'Argument [--new] invalid! File name is invalid. Must be more than five (5) characters.'


def test_validator_input_profile_new_file_already_exist_error():
    new_file = 'new.json'

    if not Settings.Base.path_profile.exists():
        makedirs(str(Settings.Base.path_profile))
    Settings.Base.path_profile.joinpath(new_file).touch()

    try:
        InputProfile(**{"new": 'new.json'})
    except ErrorArgumentIsInvalid as error:
        error.__class__ == ErrorArgumentIsInvalid
        assert str(error) == 'Argument [--new] invalid! Profile file already exists.'
    
    Settings.Base.path_profile.joinpath(new_file).unlink()


def test_validator_input_profile_delete_success():
    delete_file = 'delete.json'

    if not Settings.Base.path_profile.exists():
        makedirs(str(Settings.Base.path_profile))
    Settings.Base.path_profile.joinpath(delete_file).touch()

    fields = InputProfile(**{"delete": delete_file})
    assert fields.delete == Settings.Base.path_profile.joinpath(delete_file)

    Settings.Base.path_profile.joinpath(delete_file).unlink()


def test_validator_input_profile_delete_file_not_exist_error():
    delete_file = 'delete.json'

    try:
        InputProfile(**{"delete": delete_file})
    except ErrorArgumentIsInvalid as error:
        error.__class__ == ErrorArgumentIsInvalid
        assert str(error) == 'Argument [--delete] invalid! Profile file does not exist.'
