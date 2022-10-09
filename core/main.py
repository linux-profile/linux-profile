from core.base.command import BaseCommand
from core.base.error import (
    ErrorParameterIsMissing,
    ErrorInvalidValue
)
from core.commands.init import Init
from core.commands.add import Add
from core.commands.install import Install
from core.commands.uninstall import Uninstall
from core.commands.list import List


class CommandInit(BaseCommand):

    def finalize_options(self):
        pass

    def run(self) -> None:
        """Start
        """
        Init(module=self.module)


class CommandAdd(BaseCommand):

    def finalize_options(self):
        if self.module is None:
            raise ErrorParameterIsMissing("module")

        if self.module not in self.modules:
            raise ErrorInvalidValue("module")

    def run(self) -> None:
        """Start
        """
        Add(
            module=self.module,
            value=self.value
        )


class CommandInstall(BaseCommand):

    def finalize_options(self):
        if self.module is None:
            raise ErrorParameterIsMissing("module")

        if self.module not in self.modules:
            raise ErrorInvalidValue("module")

    def run(self) -> None:
        """Start
        """
        Install(
            module=self.module,
            category=self.category,
            value=self.value,
            option=self.option
        )


class CommandUninstall(BaseCommand):

    def finalize_options(self):
        if self.module is None:
            raise ErrorParameterIsMissing("module")

        if self.module not in self.modules:
            raise ErrorInvalidValue("module")

    def run(self) -> None:
        """Start
        """
        Uninstall(
            module=self.module,
            category=self.category,
            value=self.value
        )


class CommandList(BaseCommand):

    def finalize_options(self):
        if self.module is None:
            raise ErrorParameterIsMissing("module")

        if self.module not in self.modules:
            raise ErrorInvalidValue("module")

    def run(self) -> None:
        """Start
        """
        List(
            module=self.module,
            category=self.category,
            value=self.value
        )
