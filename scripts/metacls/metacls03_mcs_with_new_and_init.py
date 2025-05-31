

class MyMetaclass(type):

    def __new__(mcs, name, base, class_dict, **kwargs):
        print("metaclass __new__")
        object = super().__new__(mcs, name, base, class_dict)
        return object

    def __init__(self, name, base, class_dict, **kwargs):
        print("metaclass __init__")
        self.x = 123


class Point2d(metaclass=MyMetaclass):

    def __init__(self, x, y):
        print("class __init__")
        self.x = x
        self.y = y


if __name__ == "__main__":
    print(f"{Point2d.x=}")
