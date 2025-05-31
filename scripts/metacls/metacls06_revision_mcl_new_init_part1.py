# Based on: https://www.pythontutorial.net/python-oop/python-metaclass/


class MyMeta(type):

    def __new__(mcs, name, bases, class_dict, **kwargs):
        class_ = super().__new__(mcs, name, bases, class_dict)
        class_.MYPARAM = 12_345
        return class_


class Point2d(metaclass=MyMeta):

    def __init__(self, x, y):
        self.x = x
        self.y = y


if __name__ == "__main__":
    p = Point2d(2, 3)
    print(f"{p.MYPARAM=}")
