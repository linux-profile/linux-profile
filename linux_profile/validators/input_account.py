import re

from linux_profile.base.error import ErrorArgumentIsInvalid, ErrorOptionIsMissing
from linux_profile.base.validator import Validator

# Common weak passwords (top entries from breach databases)
_COMMON_WEAK_PASSWORDS = {
    "password", "12345678", "qwerty123", "admin123",
    "letmein1", "welcome1", "monkey12", "dragon12",
    "master12", "abc12345", "password1", "iloveyou",
}

_EMAIL_RE = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')


class InputAccount(Validator):

    def validator_email(self, value=None):
        if not value:
            raise ErrorOptionIsMissing('Email')

        # Security: validate email format
        if not _EMAIL_RE.match(value):
            raise ErrorArgumentIsInvalid(
                argument='--email',
                error="Invalid email format. Expected format: user@domain.com")

        return value

    def validator_password(self, value=None):
        if not value:
            raise ErrorOptionIsMissing('Password')

        # Security: minimum length
        if len(value) < 8:
            raise ErrorArgumentIsInvalid(
                argument='--password',
                error="Password must be at least 8 characters long.")

        # Security: reject common weak passwords
        if value.lower() in _COMMON_WEAK_PASSWORDS:
            raise ErrorArgumentIsInvalid(
                argument='--password',
                error="Password is too common. Choose a stronger password.")

        # Security: must contain at least two character types
        has_letter = bool(re.search(r'[a-zA-Z]', value))
        has_digit = bool(re.search(r'[0-9]', value))
        has_special = bool(re.search(r'[^a-zA-Z0-9]', value))

        type_count = sum([has_letter, has_digit, has_special])
        if type_count < 2:
            raise ErrorArgumentIsInvalid(
                argument='--password',
                error="Password must contain at least two of: letters, digits, special characters.")

        return value
