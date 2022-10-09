import uuid


class Validator():

    def __init__(self, **kwargs):
        self.id = uuid.uuid4().hex.upper()
        
        for arg in kwargs:
            value = kwargs.get(arg) if kwargs.get(arg) else None
            setattr(self, arg, value)

            if hasattr(self, "validator_"+arg):
                call = getattr(self, "validator_"+arg)
                setattr(self, arg, call(value))
