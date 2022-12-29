from linux_profile.base.config import BaseConfig
from linux_profile.utils.text import print_item
from linux_profile.base.file import BaseAction


class List(BaseConfig):

    def setup(self):
        """
        Defines the functions that are executed each
        time the class is instantiated.
        """
        self.load_profile()
        self.command = self.__class__.__name__.lower()
        self.action = BaseAction(self.file.get("profile"))

        func = f"{self.command }_{self.module}"
        call = getattr(self, func, self)

        call()

    def list_package(self):
        data = self.action.deep_search(
            module=self.module,
            tag=self.tag,
            key='name',
            value=self.item
        )
        for item in data:
            print_item(
                module=self.module,
                id=item.get("id", "Null"),
                tag=item.get("tag", "Null"),
                item=item.get("name", "Null"),
                description=item.get("description", "No description")
            )

    def list_alias(self):
        data = self.action.deep_search(
            module=self.module,
            tag=self.tag,
            key='name',
            value=self.item
        )
        for item in data:
            print_item(
                module=self.module,
                id=item.get("id", "Null"),
                tag=item.get("tag", "Null"),
                item=item.get("name", "Null"),
                description=item.get("description", "No description")
            )

    def list_script(self):
        data = self.action.deep_search(
            module=self.module,
            tag=self.tag,
            key='name',
            value=self.item
        )
        for item in data:
            print_item(
                module=self.module,
                id=item.get("id", "Null"),
                tag=item.get("tag", "Null"),
                item=item.get("name", "Null"),
                description=item.get("description", "No description")
            )

    def list_file(self):
        data = self.action.deep_search(
            module=self.module,
            tag=self.tag,
            key='name',
            value=self.item
        )
        for item in data:
            print_item(
                module=self.module,
                id=item.get("id", "Null"),
                tag=item.get("tag", "Null"),
                item=item.get("name", "Null"),
                description=item.get("description", "No description")
            )
