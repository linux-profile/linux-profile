from core.base.config import BaseConfig
from core.handlers.alias import HandlerAlias
from core.handlers.script import HandlerScript
from core.handlers.package import HandlerPackage
from core.base.storage import StorageQuery


class Install(BaseConfig):

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

    def install_package(self):
        data = self.query.deep_search(
            module=self.module,
            tag=self.tag,
            key='name',
            value=self.value
        )
        for item in data:
            item["command"] = self.command
            HandlerPackage(**item, **self.folder)

    def install_alias(self):
        data = self.query.deep_search(
            module=self.module,
            tag=self.tag,
            key='command',
            value=self.value
        )
        for item in data:
            HandlerAlias(**item)

    def install_script(self):
        data = self.query.deep_search(
            module=self.module,
            tag=self.tag,
            key='name',
            value=self.value
        )
        for item in data:
            HandlerScript(**item, **self.folder)