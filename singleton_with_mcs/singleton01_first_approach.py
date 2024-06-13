

class SingletonMeta(type):

    def __init__(self, *args, **kwargs):
        self._instance = None
        super().__init__(*args, **kwargs)
