from linux_profile.base.validator import Validator


class ValidatorTest(Validator):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


def test_base_validator_uuid_sucess():
    fields = ValidatorTest()

    assert len(fields.id) == 32
    assert type(int(fields.id, 32)) == int


def test_base_validator_generate_uuid_sucess():
    operation = ValidatorTest()
    uuid = operation.get_uuid()

    assert len(uuid) == 32
    assert type(int(uuid, 32)) == int    


def test_base_validator_generate_all_sucess():
    operation = ValidatorTest()
    items = operation.generate_all()

    assert len(items) == 1
    assert type(items) == list
