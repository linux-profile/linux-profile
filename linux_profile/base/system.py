class System(object):

    def __init__(self, **kwargs) -> None:
        self.debug = False
        self.sudo = 'on'
        self.command = 'exec'
        self.type = 'default'

        for arg in kwargs:
            value = kwargs.get(arg)
            setattr(self, arg, value)

        self.func = f"setup_{self.type}".replace("-", "_")
        if hasattr(self, self.func):
            getattr(self, self.func, None)()

    def setup_default(self):
        return "Method not Implemented"
