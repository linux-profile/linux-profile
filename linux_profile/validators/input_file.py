from linux_profile.base.validator import Validator
from linux_profile.utils.text import slugify
from linux_profile.base.error import ErrorOptionIsMissing


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
