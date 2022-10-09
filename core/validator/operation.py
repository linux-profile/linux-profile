from core.base.validator import Validator
from core.base.error import ErrorParameterIsMissing


class OperationInstallScript(Validator):

    def validator_category(self, value = None):
        if not value:
            raise ErrorParameterIsMissing("category")

    def validator_value(self, value = None):
        if not value:
            raise ErrorParameterIsMissing("value")
