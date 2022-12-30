from linux_profile.base.validator import Validator
from linux_profile.utils.text import slugify, cleaning_option
from linux_profile.base.error import (
    ErrorOptionIsMissing,
    ErrorInvalidValue,
    ErrorOptionIsInvalid
)


class InputAddScript(Validator):

    types = [
        'shell',
        'python',
        'python3',
        'ruby'
    ]

    def validator_tag(self, value=None):
        return slugify(value) if value else 'default'

    def validator_type(self, value=None):
        if not value:
            raise ErrorOptionIsMissing('Script Type')

        if value not in self.types:
            raise ErrorOptionIsInvalid('Script Type', self.types)

        return slugify(value=value, slug_type='-')

    def validator_name(self, value=None):
        if not value:
            raise ErrorOptionIsMissing('Script Name')

        return slugify(value)

    def validator_description(self, value=None):
        value = value if value else 'No description'
        if len(value) > 85:
            raise ErrorInvalidValue("Script Description")

        return cleaning_option(value)
