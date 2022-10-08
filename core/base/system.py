class System(object):

    def __init__(self, **kwargs) -> None:
        for arg in kwargs:
            value = kwargs.get(arg)
            setattr(self, arg, value)

        self.func = f"setup_{self.type}".replace("-", "_")
        if hasattr(self, self.func):
            getattr(self, self.func, None)()
