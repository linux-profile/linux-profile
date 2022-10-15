import uuid

from linux_profile.utils.text import slugify, cleaning_option
from linux_profile.base.error import (
    ErrorOptionIsMissing,
    ErrorInvalidValue,
    ErrorOptionIsInvalid
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

    def validator_tag(self, value = None):
        return slugify(value) if value else 'default'

    def validator_type(self, value = None):
        if not value:
            raise ErrorOptionIsMissing('Package Manager')

        if not value in self.types:
            raise ErrorOptionIsInvalid('Package Type', self.types)

        return slugify(value=value, slug_type='-')

    def validator_name(self, value = None):
        if not value:
            raise ErrorOptionIsMissing('Package Name')

        return cleaning_option(value)

    def validator_description(self, value = None):
        value = value if value else 'No description'
        if len(value) > 85:
            raise ErrorInvalidValue("Package Description")

        return cleaning_option(value)


class InputAddAlias(Validator):

    def validator_tag(self, value = None):
        return slugify(value) if value else 'default'

    def validator_name(self, value = None):
        if not value:
            raise ErrorOptionIsMissing('Alias Name')

        return slugify(value)

    def validator_command(self, value = None):
        if not value:
            raise ErrorOptionIsMissing('Alias Command')

        return slugify(value)

    def validator_body(self, value = None):
        if not value:
            raise ErrorOptionIsMissing('Alias Body')

        return value

    def validator_description(self, value = None):
        value = value if value else 'No description'
        if len(value) > 85:
            raise ErrorInvalidValue("Alias Description")

        return cleaning_option(value)


class InputAddTerminal(Validator):

    def validator_tag(self, value = None):
        return slugify(value) if value else 'default'

    def validator_name(self, value = None):
        if not value:
            raise ErrorOptionIsMissing('Terminal Name')

        return slugify(value)

    def validator_description(self, value = None):
        value = value if value else 'No description'
        if len(value) > 85:
            raise ErrorInvalidValue("Terminal Description")

        return cleaning_option(value)


class InputAddScript(Validator):

    types = [
        'shell',
        'python',
        'python3',
        'ruby'
    ]

    def validator_tag(self, value = None):
        return slugify(value) if value else 'default'

    def validator_type(self, value = None):
        if not value:
            raise ErrorOptionIsMissing('Script Type')

        if not value in self.types:
            raise ErrorOptionIsInvalid('Script Type', self.types)

        return slugify(value=value, slug_type='-')

    def validator_name(self, value = None):
        if not value:
            raise ErrorOptionIsMissing('Script Name')

        return slugify(value)

    def validator_description(self, value = None):
        value = value if value else 'No description'
        if len(value) > 85:
            raise ErrorInvalidValue("Script Description")

        return cleaning_option(value)
