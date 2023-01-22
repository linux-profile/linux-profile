from linux_profile.base.action import Action
from linux_profile.base.settings import Settings
from linux_profile.handlers.alias import HandlerAlias
from linux_profile.handlers.script import HandlerScript
from linux_profile.handlers.package import HandlerPackage


class Install(Settings):

    def setup(self):
        """Defines the functions that are executed each
        time the class is instantiated.
        """
        self.command = self.__class__.__name__.lower()
        self.action = Action(
            str(self.path_profile.joinpath(self.file_profile)))

        func = self.join(value=[self.command, self.module], separator="_")
        getattr(self, func, self)()

    def install_package(self):
        data = self.action.deep_search(
            module=self.module,
            tag=self.tag,
            key='name',
            value=self.item
        )

        if self.group:
            type_packages = {}
            for item in data:
                item_type = item["type"]
                if not type_packages.get(item_type):
                    item_name = []
                    type_packages[item_type] = dict(
                        type=item_type,
                        name=item_name,
                        command=self.command
                    )
                item_name.append(item["name"])

            for package in type_packages:
                data_package = type_packages.get(package)
                data_package["name"] = " ".join(data_package.get("name"))
                HandlerPackage(
                    sudo=self.sudo,
                    debug=self.debug,
                    **data_package)

        else:
            for item in data:
                item["command"] = self.command
                HandlerPackage(
                    sudo=self.sudo,
                    debug=self.debug,
                    **item)

    def install_alias(self):
        data = self.action.deep_search(
            module=self.module,
            tag=self.tag,
            key='command',
            value=self.item
        )
        for item in data:
            HandlerAlias(
                sudo=self.sudo,
                debug=self.debug,
                **item)

    def install_script(self):
        data = self.action.deep_search(
            module=self.module,
            tag=self.tag,
            key='name',
            value=self.item
        )
        for item in data:
            HandlerScript(
                sudo=self.sudo,
                debug=self.debug,
                **item,
                **dict(temp=self.path_temp))
