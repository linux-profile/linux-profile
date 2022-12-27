from linux_profile.base.system import System


class SystemTest(System):

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

    def setup_exec(self):
        pass


def test_base_system_func():
    item = SystemTest(type="exec")
    assert item.func == 'setup_exec'
