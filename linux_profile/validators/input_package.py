from linux_profile.base.validator import Validator
from linux_profile.utils.text import slugify, cleaning_option
from linux_profile.base.error import (
    ErrorOptionIsMissing,
    ErrorInvalidValue,
    ErrorOptionIsInvalid
)


class InputAddPackage(Validator):

    types = [
        'apt-get',
        'apt',
        'snap',
        'yum',
        'dnf',
        'pacman',
        'zypper',
        'spack',
        'brew',
        'pip',
        'shell',
        'deb'
    ]

    def validator_tag(self, value = None):
        return slugify(value) if value else 'default'

    def validator_type(self, value = None):
        if not value:
            raise ErrorOptionIsMissing('Package Manager')

        if not value in self.types:
            raise ErrorOptionIsInvalid('Package Type', self.types)

        return slugify(value=value, slug_type='-')

    def validator_name(self, value = None):
        if not value:
            raise ErrorOptionIsMissing('Package Name')

        return cleaning_option(value)

    def validator_description(self, value = None):
        value = value if value else 'No description'
        if len(value) > 85:
            raise ErrorInvalidValue("Package Description")

        return cleaning_option(value)

    def generate_all(self):
        list_packages = []
        fields = self.__dict__
        fields_name = fields.get("name").split(",")

        for field in fields_name:
            new_fields = dict(
                id=self.get_uuid(),
                tag=self.tag,
                type=self.type,
                name=cleaning_option(field),
                url=self.url,
                file=self.file,
                description=self.description
            )
            list_packages.append(new_fields)
        return list_packages
