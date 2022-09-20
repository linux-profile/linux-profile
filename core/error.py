class ErrorLoadSettings(Exception):

    def __init__(self,
                 message="It is not possible to load the basic settings."):
        super(ErrorLoadSettings, self).__init__(message)
