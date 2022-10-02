import uuid

from core.utils.text import cleaning_option
from core.base.error import (
    print_option_is_missing,
    print_option_invalid_value
)


class Validator():

    def __init__(self, *args, **kwargs):
        self.id = uuid.uuid4().hex.upper()
        self.is_valid = True

        for arg in kwargs:
            if hasattr(self, "validator_"+arg):
                call = getattr(self, "validator_"+arg)
                setattr(self, arg, call(kwargs.get(arg)))


class ValidatorAddPackage(Validator):

    def validator_category(self, value = None):
        return value.lower() if value else 'default'

    def validator_manager(self, value = None):
        if not value:
            print_option_is_missing(parameter='Package Manager')
            self.is_valid = False

        if not value in ['apt-get', 'snap', 'deb']:
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

        return cleaning_option(value)


class ValidatorAddTerminal(Validator):

    def validator_category(self, value = None):
        return value.lower() if value else 'default'

    def validator_name(self, value = None):
        if not value:
            print_option_is_missing(parameter='Terminal Name')
            self.is_valid = False

        return cleaning_option(value).lower()
