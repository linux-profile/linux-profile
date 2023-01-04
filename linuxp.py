#!/usr/bin/env python3

import argparse

from linux_profile.base.command import BaseCommand, Command

from linux_profile.commands.add import Add
from linux_profile.commands.config import Config
from linux_profile.commands.execute import Execute
from linux_profile.commands.install import Install
from linux_profile.commands.uninstall import Uninstall
from linux_profile.commands.list import List
from linux_profile.commands.remove import Remove


class CommandConfig(Command):

    def execute(self):
        """Start"""
        Config(**self.arguments.__dict__)


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
                item=self.item
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
                item=self.item
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


def main():
    parser = argparse.ArgumentParser(description='Linux profile management tool')
    command = BaseCommand(parser)

    command.cmd_config.set_defaults(exec=CommandConfig)
    command.cmd_add.set_defaults(exec=CommandAdd)
    command.cmd_remove.set_defaults(exec=CommandRemove)
    command.cmd_execute.set_defaults(exec=CommandExecute)
    command.cmd_install.set_defaults(exec=CommandInstall)
    command.cmd_uninstall.set_defaults(exec=CommandUninstall)
    command.cmd_list.set_defaults(exec=CommandList)

    command.run()


if __name__ == '__main__':
    main()
