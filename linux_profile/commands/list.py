from linux_profile.base.action import Action
from linux_profile.base.config import Config
from linux_profile.utils.text import print_item


class List(Config):

    def setup(self):
        """Defines the functions that are executed each
        time the class is instantiated.
        """
        self.command = self.__class__.__name__.lower()
        self.action = Action(
            self.join([self.linuxp_path_config, self.linuxp_file_profile]))

        func = self.join(value=[self.command, self.module], separator="_")
        getattr(self, func, self)()

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
