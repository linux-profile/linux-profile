from linux_profile.base.settings import Settings


class Execute(Settings):

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        print("Error: 'execute' command is not yet implemented.")
        print("See https://github.com/linux-profile/linux-profile for updates.")
