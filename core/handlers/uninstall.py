from core.base.config import BaseConfig
from core.modules.package import SystemPackage


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

        func = f"{self.command }_{self.module}"
        call_add = getattr(self, func)
        call_add()

    def uninstall_package(self):
        if self.category:
            for item in self.profile[self.module][self.category]:
                item["command"] = self.command
                SystemPackage(**item)
        else:
            for category in self.profile[self.module]:
                for item in self.profile[self.module][category]:
                    item["command"] = self.command
                    SystemPackage(**item)
