#!/usr/bin/env python3

from core.handlers.init import Init
from core.handlers.add import Add
from core.handlers.sync import Sync

from core.base import BaseCommand


class CommandInit(BaseCommand):

    def run(self):
        Init()


class CommandAdd(BaseCommand):

    def run(self):
        Add()


class CommandSync(BaseCommand):

    def run(self):
        Sync()
