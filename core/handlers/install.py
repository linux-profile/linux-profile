from core.base.config import BaseConfig
from core.modules.alias import SystemAlias
from core.modules.script import SystemScript
from core.modules.package import SystemPackage

from core.base.storage import StorageQuery
from core.validator.operation import OperationInstallScript


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

        func = f"{self.command }_{self.module}"
        call_add = getattr(self, func)
        call_add()

    def install_package(self):
        if self.category:
            for item in self.profile[self.module].get(self.category, []):
                item["command"] = self.command
                SystemPackage(**item)
        else:
            for _tag in self.profile[self.module]:
                for item in self.profile[self.module][_tag]:
                    item["command"] = self.command
                    SystemPackage(**item)

    def install_alias(self):
        if self.category:
            for item in self.profile[self.module].get(self.category, []):
                SystemAlias(**item)
        else:
            for _tag in self.profile[self.module]:
                for item in self.profile[self.module][_tag]:
                    SystemAlias(**item)

    def install_script(self):
        OperationInstallScript(**self.__dict__)
        query = StorageQuery(self.file.get("profile"))

        if self.value:
            item = query.key(
                module=self.module,
                tag=self.category,
                key='name',
                value=self.value
            )
            if item:
                SystemScript(**item, **self.folder)
        else:
            items = query.tag(
                module=self.module,
                tag=self.category
            )
            if items:
                for item in items:
                    SystemScript(**item, **self.folder)
