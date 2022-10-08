#!/usr/bin/env python3

from core.base.command import BaseCommand
from core.base.error import (
    ErrorParameterIsMissing,
    ErrorInvalidValue,
    ErrorLoadSettings
)
from core.handlers.init import Init
from core.handlers.add import Add
from core.handlers.install import Install
from core.handlers.uninstall import Uninstall


class CommandInit(BaseCommand):

    def finalize_options(self):
        pass

    def run(self) -> None:
        """Start
        """
        try:
            Init(module=self.module)
        except Exception:
            raise ErrorLoadSettings()


class CommandAdd(BaseCommand):

    def finalize_options(self):
        if self.module is None:
            raise ErrorParameterIsMissing("module")

        if self.module not in self.modules:
            raise ErrorInvalidValue("module")

    def run(self) -> None:
        """Start
        """
        try:
            Add(
                module=self.module,
                value=self.value
            )
        except Exception:
            raise ErrorLoadSettings()


class CommandInstall(BaseCommand):

    def finalize_options(self):
        if self.module is None:
            raise ErrorParameterIsMissing("module")

        if self.module not in self.modules:
            raise ErrorInvalidValue("module")

    def run(self) -> None:
        """Start
        """
        try:
            Install(
                module=self.module,
                category=self.category,
                value=self.value
            )
        except Exception:
            raise ErrorLoadSettings()


class CommandUninstall(BaseCommand):

    def run(self) -> None:
        """Start
        """
        try:
            Uninstall(
                module=self.module,
                category=self.category,
                value=self.value
            )
        except Exception:
            raise ErrorLoadSettings()
