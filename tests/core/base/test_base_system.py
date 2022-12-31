from linux_profile.base.system import System


class SystemTest(System):

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)


def test_base_system_no_specific_method():
    item = SystemTest()
    assert item.func == "setup_default"


def test_base_system_with_specific_method():
    item = SystemTest(type="specific")
    assert item.func == "setup_specific"


def test_base_system_standard_variables_check():
    item = SystemTest()
    assert item.debug == False
    assert item.sudo == False
    assert item.command == 'exec'
    assert item.type == 'default'
