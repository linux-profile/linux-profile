from linux_profile.base.validator import Validator
from linux_profile.utils.text import slugify
from linux_profile.base.error import ErrorOptionIsMissing


class InputAddText(Validator):

    def validator_tag(self, value=None):
        return slugify(value) if value else 'default'

    def validator_name(self, value=None):
        if not value:
            raise ErrorOptionIsMissing('Name')
        return slugify(value)

    def validator_text(self, value=None):
        if not value:
            raise ErrorOptionIsMissing('Text')
        return value

    def validator_label(self, value=None):
        if not value:
            return list()
        return value.split(",")
