#!/usr/bin/env python3

from core.base.command import BaseCommand
from core.error import (
    print_error_settings,
    print_parameter_is_missing,
    print_error_invalid_value,
    ErrorParameterIsMissing,
    ErrorInvalidValue
)

from core.handlers.init import Init
from core.handlers.add import Add
from core.handlers.sync import Sync


class CommandInit(BaseCommand):

    def finalize_options(self):
        pass

    def run(self) -> None:
        """Start
        """
        try:
            Init(module=self.module)
        except Exception as error:
            print_error_settings()


class CommandAdd(BaseCommand):

    def run(self) -> None:
        """Start
        """
        try:
            Add(
                module=self.module,
                value=self.value
            )
        except Exception as error:
            print_error_settings()


class CommandSync(BaseCommand):

    def finalize_options(self):
        if self.module is None:
            print_parameter_is_missing("module")

        if self.module not in self.modules:
            print_error_invalid_value("module")

    def run(self) -> None:
        """Start
        """
        try:
            Sync(module=self.module)
        except Exception as error:
            print_error_settings()
