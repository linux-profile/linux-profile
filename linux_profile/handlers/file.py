from linux_profile.base.system import System


class HandlerFile(System):

    def setup_update(self) -> None:
        raise NotImplementedError(
            f"{self.__class__.__name__} must implement setup_update()"
        )
