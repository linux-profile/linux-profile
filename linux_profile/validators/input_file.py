from linux_profile.base.validator import Validator
from linux_profile.utils.text import slugify, cleaning_option
from linux_profile.base.error import (
    ErrorOptionIsMissing,
    ErrorInvalidValue
)


class InputAddFile(Validator):

    def validator_tag(self, value=None):
        return slugify(value) if value else 'default'

    def validator_name(self, value=None):
        if not value:
            raise ErrorOptionIsMissing('File Name')
        return value

    def validator_file_path(self, value=None):
        if not value:
            raise ErrorOptionIsMissing('File Path')
        return value

    def validator_description(self, value=None):
        value = value if value else 'No description'
        if len(value) > 85:
            raise ErrorInvalidValue("File Description")
        return cleaning_option(value)
