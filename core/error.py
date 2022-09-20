class ErrorLoadSettings(Exception):

    def __init__(self,
                 message="It is not possible to load the basic settings."):
        super(ErrorLoadSettings, self).__init__(message)


class ErrorParameterIsMissing(Exception):

    def __init__(self, parameter):
        super(ErrorParameterIsMissing, self).__init__(
            "Parameter --{} is missing".format(parameter))


class ErrorInvalidValue(Exception):

    def __init__(self, parameter):
        super(ErrorInvalidValue, self).__init__(
            "Parameter --{} invalid value".format(parameter))
