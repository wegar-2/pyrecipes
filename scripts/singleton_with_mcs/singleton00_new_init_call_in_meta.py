

class SingletonMeta(type):

    _INSTANCES_VAULT: dict = {}

    def __call__(cls, *args, **kwargs):
        if cls not in SingletonMeta._INSTANCES_VAULT:
            print(f"Creating the single instance of class {cls}")
            instance = super(SingletonMeta, cls).__call__(*args, **kwargs)
            SingletonMeta._INSTANCES_VAULT[cls] = instance
            return instance
        else:
            print("Modifying the single existing object...")
            instance = SingletonMeta._INSTANCES_VAULT[cls]
            cls.__init__(instance, *args, **kwargs)
            SingletonMeta._INSTANCES_VAULT[cls] = instance
            return instance


class Point2d(metaclass=SingletonMeta):
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Value(metaclass=SingletonMeta):
    def __init__(self, value):
        self.value = value


class Container(metaclass=SingletonMeta):
    pass


if __name__ == "__main__":

    v = Value("asdf")

    p1 = Point2d(10, 23)
    p2 = Point2d(100, 23)
    print(f"{(p1 is p2)=}")

    c1 = Container()
    c2 = Container()
    print(f"{(c1 is c2)=}")
