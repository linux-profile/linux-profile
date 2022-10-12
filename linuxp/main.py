
from linuxp.base.command import BaseCommand
from linuxp.base.error import (
    ErrorParameterIsMissing,
    ErrorInvalidValue
)
from linuxp.commands.init import Init
from linuxp.commands.add import Add
from linuxp.commands.install import Install
from linuxp.commands.uninstall import Uninstall
from linuxp.commands.list import List


class CommandInit(BaseCommand):

    def finalize_options(self):
        pass

    def run(self):
        """Start
        """
        super().run()
        Init(module=self.module)
        

class CommandAdd(BaseCommand):

    def finalize_options(self):
        if '--help' in self.distribution.script_args:
            return

        if self.module is None:
            raise ErrorParameterIsMissing("module")

        if self.module not in self.modules:
            raise ErrorInvalidValue("module")

    def run(self) -> None:
        """Start
        """
        super().run()
        Add(
            module=self.module,
            value=self.value
        )


class CommandInstall(BaseCommand):

    def finalize_options(self):
        if '--help' in self.distribution.script_args:
            return

        if self.module is None:
            raise ErrorParameterIsMissing("module")

        if self.module not in self.modules:
            raise ErrorInvalidValue("module")

    def run(self) -> None:
        """Start
        """
        super().run()
        Install(
            module=self.module,
            tag=self.tag,
            value=self.value,
            option=self.option
        )


class CommandUninstall(BaseCommand):

    def finalize_options(self):
        if '--help' in self.distribution.script_args:
            return

        if self.module is None:
            raise ErrorParameterIsMissing("module")

        if self.module not in self.modules:
            raise ErrorInvalidValue("module")

    def run(self) -> None:
        """Start
        """
        super().run()
        Uninstall(
            module=self.module,
            tag=self.tag,
            value=self.value
        )


class CommandList(BaseCommand):

    def finalize_options(self):
        if '--help' in self.distribution.script_args:
            return

        if self.module is None:
            raise ErrorParameterIsMissing("module")

        if self.module not in self.modules:
            raise ErrorInvalidValue("module")

    def run(self) -> None:
        """Start
        """
        super().run()
        List(
            module=self.module,
            tag=self.tag,
            value=self.value
        )


def main():
    print("linuxp --versio 1.0.0.")