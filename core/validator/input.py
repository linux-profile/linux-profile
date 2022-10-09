from core.base.validator import Validator
from core.utils.text import cleaning_option
from core.base.error import ErrorOptionIsMissing


class InputAddPackage(Validator):

    types = [
        'apt-get',
        'apt',
        'snap',
        'deb',
        'sh',
        'py',
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
        'bash',
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
