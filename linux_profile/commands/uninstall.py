from linux_profile.base.action import Action
from linux_profile.base.config import Config
from linux_profile.handlers.package import HandlerPackage


class Uninstall(Config):

    def setup(self):
        """Defines the functions that are executed each
        time the class is instantiated.
        """
        self.command = self.__class__.__name__.lower()
        self.action = Action(
            self.join([self.linuxp_path_config, self.linuxp_file_profile]))

        func = self.join(value=[self.command, self.module], separator="_")
        getattr(self, func, self)()

    def uninstall_package(self):
        data = self.action.deep_search(
            module=self.module,
            tag=self.tag,
            key='name',
            value=self.item
        )
        for item in data:
            item["command"] = self.command
            HandlerPackage(sudo=self.sudo, debug=self.debug, **item)
