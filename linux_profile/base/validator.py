import uuid

from linux_profile.utils.text import cleaning_option
from linux_profile.base.error import ErrorOptionIsMissing


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
        'deb',
        'shell',
        'dnf',
        'pacman',
        'zypper',
        'spack',
        'brew',
        'pip'
    ]

    def validator_category(self, value = None):
        return value.lower() if value else 'default'

    def validator_type(self, value = None):
        if not value:
            raise ErrorOptionIsMissing('Package Manager')

        if not value in self.types:
            raise ErrorOptionIsMissing('Package Manager')

        return cleaning_option(value).lower()

    def validator_name(self, value = None):
        if not value:
            raise ErrorOptionIsMissing('Package name')

        return cleaning_option(value)


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


class InputAddTerminal(Validator):

    def validator_category(self, value = None):
        return value.lower() if value else 'default'

    def validator_name(self, value = None):
        if not value:
            raise ErrorOptionIsMissing('Terminal Name')

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
            raise ErrorOptionIsMissing('Script Type')

        return cleaning_option(value).lower()

    def validator_name(self, value = None):
        if not value:
            raise ErrorOptionIsMissing('Script name')

        return cleaning_option(value)


class InputInitConfig(Validator):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
