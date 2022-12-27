from linux_profile.validators.input_alias import InputAddAlias


def test_validator_input_alias_tag_default():
    fields = InputAddAlias(**{"tag": None})
    assert fields.tag == 'default'


def test_validator_input_alias_tag_underline():
    fields = InputAddAlias(**{"tag": 'linux profile'})
    assert fields.tag == 'linux_profile'


def test_validator_input_alias_tag_lower():
    fields = InputAddAlias(**{"tag": 'LINUXPROFILE'})
    assert fields.tag == 'linuxprofile'
