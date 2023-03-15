#!/usr/bin/env python3

import argparse

from linux_profile.base.command import BaseCommand, Command

from linux_profile.commands.account import Account
from linux_profile.commands.add import Add
from linux_profile.commands.config import Config
from linux_profile.commands.profile import Profile
from linux_profile.commands.execute import Execute
from linux_profile.commands.install import Install
from linux_profile.commands.uninstall import Uninstall
from linux_profile.commands.list import List
from linux_profile.commands.remove import Remove


class CommandConfig(Command):

    def execute(self):
        """Start"""
        Config(**self.arguments.__dict__)


class CommandProfile(Command):

    def execute(self):
        """Start"""
        Profile(**self.arguments.__dict__)


class CommandAdd(Command):

    def execute(self) -> None:
        """Start"""
        Add(**dict(module=self.module))


class CommandRemove(Command):

    def execute(self) -> None:
        """Start"""
        Remove(**dict(id=self.id))


class CommandExecute(Command):

    def execute(self) -> None:
        """Start"""
        Execute(**dict(id=self.id))


class CommandInstall(Command):

    def execute(self) -> None:
        """Start"""
        Install(
            **dict(
                sudo=self.sudo,
                debug=self.debug,
                module=self.module,
                tag=self.tag,
                item=self.item,
                group=self.group
            )
        )


class CommandUninstall(Command):

    def execute(self) -> None:
        """Start"""
        Uninstall(
            **dict(
                sudo=self.sudo,
                debug=self.debug,
                module=self.module,
                tag=self.tag,
                item=self.item,
                group=self.group
            )
        )


class CommandList(Command):

    def execute(self) -> None:
        """Start"""
        List(
            **dict(
                module=self.module,
                tag=self.tag,
                item=self.item
            )
        )


class CommandAccount(Command):

    def execute(self):
        """Start"""
        Account(**self.arguments.__dict__)


class BuildCommand:

    base_command = BaseCommand

    def __init__(self) -> None:
        parser = argparse.ArgumentParser(description='🐧 Linux Profile Management CLI Tool')
        self.command = self.base_command(parser)
        self.core_commands()
        self.command.run()

    def core_commands(self):
        self.command.cmd_config.set_defaults(exec=CommandConfig)
        self.command.cmd_profile.set_defaults(exec=CommandProfile)
        self.command.cmd_add.set_defaults(exec=CommandAdd)
        self.command.cmd_remove.set_defaults(exec=CommandRemove)
        self.command.cmd_execute.set_defaults(exec=CommandExecute)
        self.command.cmd_install.set_defaults(exec=CommandInstall)
        self.command.cmd_uninstall.set_defaults(exec=CommandUninstall)
        self.command.cmd_list.set_defaults(exec=CommandList)
        self.setup()

    def setup(self) -> str:
        return "Method not Implemented"


def main():
    BuildCommand()


if __name__ == '__main__':
    main()
