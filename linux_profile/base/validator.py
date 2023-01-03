"""
Module Validator
"""


import uuid


class Validator():

    def __init__(self, **kwargs):
        self.id = self.get_uuid()

        for arg in kwargs:
            value = kwargs.get(arg) if kwargs.get(arg) else None
            setattr(self, arg, value)

            if hasattr(self, "validator_" + arg):
                call = getattr(self, "validator_" + arg)
                setattr(self, arg, call(value))

    def get_uuid(self):
        return uuid.uuid4().hex.upper()

    def generate_all(self):
        return [self.__dict__]
