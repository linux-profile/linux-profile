import uuid

from core.utils.text import cleaning_option
from core.base.error import (
    print_option_is_missing,
    print_option_invalid_value
)


class Validator():

    def __init__(self, **kwargs):
        self.id = uuid.uuid4().hex.upper()
        self.is_valid = True
        
        for arg in kwargs:
            value = kwargs.get(arg) if kwargs.get(arg) else None
            setattr(self, arg, value)

            if hasattr(self, "validator_"+arg):
                call = getattr(self, "validator_"+arg)
                setattr(self, arg, call(value))


class ValidatorAddPackage(Validator):

    option_manager = [
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
            print_option_is_missing(parameter='Package Manager '+ str(self.option_manager))
            self.is_valid = False

        if not value in self.option_manager:
            print_option_invalid_value(parameter='Package Manager')
            self.is_valid = False

        return cleaning_option(value).lower()

    def validator_name(self, value = None):
        if not value:
            print_option_is_missing(parameter='Package name')
            self.is_valid = False

        return cleaning_option(value)


class ValidatorAddAlias(Validator):

    def validator_category(self, value = None):
        return value.lower() if value else 'default'

    def validator_command(self, value = None):
        if not value:
            print_option_is_missing(parameter='Alias Command')
            self.is_valid = False

        return cleaning_option(value).lower()

    def validator_content(self, value = None):
        if not value:
            print_option_is_missing(parameter='Alias Content')
            self.is_valid = False

        return value


class ValidatorAddTerminal(Validator):

    def validator_category(self, value = None):
        return value.lower() if value else 'default'

    def validator_name(self, value = None):
        if not value:
            print_option_is_missing(parameter='Terminal Name')
            self.is_valid = False

        return value


class ValidatorInitDefault(Validator):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class ValidatorInitConfig(Validator):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
