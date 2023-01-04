from linux_profile.base.validator import Validator
from linux_profile.utils.text import slugify, cleaning_option
from linux_profile.base.error import (
    ErrorOptionIsMissing,
    ErrorOptionIsInvalid
)


class InputAddFile(Validator):

    types = [
        "create",
        "read",
        "update",
        "delete"
    ]

    def validator_tag(self, value=None):
        return slugify(value) if value else 'default'

    def validator_type(self, value=None):
        if not value:
            raise ErrorOptionIsMissing('File Operation Type ')

        if value not in self.types:
            raise ErrorOptionIsInvalid('File Operation Type ', self.types)

        return cleaning_option(value)
