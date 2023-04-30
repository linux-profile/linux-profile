from urllib.parse import urlsplit

from linux_profile.base.validator import Validator
from linux_profile.base.error import (
    ErrorArgumentIsInvalid,
    ErrorOptionIsMissing
)

class InputConfig(Validator):

    def validator_url(self, value=None):
        if value:
            if urlsplit(value).scheme not in ["http", "https"]:
                raise ErrorArgumentIsInvalid(
                    argument='--url',
                    error="The URL must have http or https.")
        return value

    def validator_editor(self, value=None):
        if not value:
            raise ErrorOptionIsMissing('Editor Name')
        return value
