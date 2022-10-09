from core.base.config import BaseConfig
from core.utils.text import print_item
from core.base.storage import StorageQuery


class List(BaseConfig):

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

    def list_package(self):
        data = self.query.deep_search(
            module=self.module,
            tag=self.tag,
            key='name',
            value=self.value
        )
        for item in data:
            print_item(self.module, item["tag"], item["name"])

    def list_alias(self):
        data = self.query.deep_search(
            module=self.module,
            tag=self.tag,
            key='command',
            value=self.value
        )
        for item in data:
            print_item(self.module, item["tag"], item["command"])

    def list_script(self):
        data = self.query.deep_search(
            module=self.module,
            tag=self.tag,
            key='name',
            value=self.value
        )
        for item in data:
            print_item(self.module, item["tag"], item["name"])
