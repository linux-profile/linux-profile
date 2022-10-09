from core.base.config import BaseConfig
from core.handlers.package import HandlerPackage
from core.base.storage import StorageQuery


class Uninstall(BaseConfig):

    def setup(self):
        """
        Defines the functions that are executed each
        time the class is instantiated.
        """
        self.add_config()
        self.load_config()
        self.load_profile()
        self.command = self.__class__.__name__.lower()
        self.query = StorageQuery(self.file.get("profile"))

        func = f"{self.command }_{self.module}"
        call = getattr(self, func, self)
        call()

    def uninstall_package(self):
        data = self.query.deep_search(
            module=self.module,
            tag=self.tag,
            key='name',
            value=self.value
        )
        for item in data:
            item["command"] = self.command
            HandlerPackage(**item)
