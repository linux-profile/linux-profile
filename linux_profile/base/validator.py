import uuid

from linux_profile.utils.text import cleaning_option
from linux_profile.base.error import (
    ErrorOptionIsMissing,
    ErrorInvalidValue,
    ErrorInvalidOption
)


class Validator():

    def __init__(self, **kwargs):
        self.id = uuid.uuid4().hex.upper()
        
        for arg in kwargs:
            value = kwargs.get(arg) if kwargs.get(arg) else None
            setattr(self, arg, value)

            if hasattr(self, "validator_"+arg):
                call = getattr(self, "validator_"+arg)
                setattr(self, arg, call(value))


class InputAddPackage(Validator):

    types = [
        'apt-get',
        'apt',
        'snap',
        'yum',
        'dnf',
        'pacman',
        'zypper',
        'spack',
        'brew',
        'pip',
        'shell',
        'deb'
    ]

    def validator_category(self, value = None):
        return value.lower() if value else 'default'

    def validator_type(self, value = None):
        if not value:
            raise ErrorOptionIsMissing('Package Manager')

        if not value in self.types:
            raise ErrorInvalidOption('Package Type', self.types)

        return cleaning_option(value).lower()

    def validator_name(self, value = None):
        if not value:
            raise ErrorOptionIsMissing('Package name')

        return cleaning_option(value)

    def validator_description(self, value = None):
        value = value if value else 'No description'
        if len(value) > 85:
            raise ErrorInvalidValue("Package Description")

        return value


class InputAddAlias(Validator):

    def validator_category(self, value = None):
        return value.lower() if value else 'default'

    def validator_command(self, value = None):
        if not value:
            raise ErrorOptionIsMissing('Alias Command')

        return cleaning_option(value).lower()

    def validator_body(self, value = None):
        if not value:
            raise ErrorOptionIsMissing('Alias Body')

        return value

    def validator_description(self, value = None):
        value = value if value else 'No description'
        if len(value) > 85:
            raise ErrorInvalidValue("Alias Description")

        return value


class InputAddTerminal(Validator):

    def validator_category(self, value = None):
        return value.lower() if value else 'default'

    def validator_name(self, value = None):
        if not value:
            raise ErrorOptionIsMissing('Terminal Name')

        return value

    def validator_description(self, value = None):
        value = value if value else 'No description'
        if len(value) > 85:
            raise ErrorInvalidValue("Terminal Description")

        return value


class InputAddScript(Validator):

    types = [
        'shell',
        'python',
        'python3',
        'ruby'
    ]

    def validator_category(self, value = None):
        return value.lower() if value else 'default'

    def validator_type(self, value = None):
        if not value:
            raise ErrorOptionIsMissing('Script Type')

        if not value in self.types:
            raise ErrorInvalidOption('Script Type', self.types)

        return cleaning_option(value).lower()

    def validator_name(self, value = None):
        if not value:
            raise ErrorOptionIsMissing('Script name')

        return cleaning_option(value)

    def validator_description(self, value = None):
        value = value if value else 'No description'
        if len(value) > 85:
            raise ErrorInvalidValue("Script Description")

        return value
