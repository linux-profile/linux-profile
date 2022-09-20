#!/usr/bin/env python3

from core.base.command import BaseCommand
from core.error import ErrorLoadSettings

from core.handlers.init import Init
from core.handlers.add import Add
from core.handlers.sync import Sync


class CommandInit(BaseCommand):

    def run(self) -> None:
        """Start
        """
        try:
            Init(module=self.module)
        except Exception as error:
            raise ErrorLoadSettings() from error


class CommandAdd(BaseCommand):

    def finalize_options(self):
        if self.module is None:
            raise Exception("Parameter --module is missing")

        if self.module not in self.modules:
            raise Exception("Parameter --module invalid value")

    def run(self) -> None:
        """Start
        """
        try:
            Add(module=self.module)
        except Exception as error:
            raise ErrorLoadSettings() from error


class CommandSync(BaseCommand):

    def finalize_options(self):
        if self.module is None:
            raise Exception("Parameter --module is missing")

        if self.module not in self.modules:
            raise Exception("Parameter --module invalid value")

    def run(self) -> None:
        """Start
        """
        try:
            Sync(module=self.module)
        except Exception as error:
            raise ErrorLoadSettings() from error
