#!/usr/bin/env python

from base import BaseCommand


class Init(BaseCommand):

    def run(self):
        print("Command: Init")


class Add(BaseCommand):

    def run(self):
        print("Command: Add")

    
class Sync(BaseCommand):

    def run(self):
        print("Command: Sync")
