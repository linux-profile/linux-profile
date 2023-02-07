from linux_profile.base.error import ErrorOptionIsMissing
from linux_profile.base.validator import Validator


class InputAccount(Validator):

    def validator_email(self, value=None):
        if not value:
            raise ErrorOptionIsMissing('Email')
        return value

    def validator_password(self, value=None):
        if not value:
            raise ErrorOptionIsMissing('Password')
        return value
