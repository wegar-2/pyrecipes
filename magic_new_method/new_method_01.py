# sources:
# (1) https://medium.com/@zackbunch/when-to-use-new-in-python-58632249b9cc
# (2) https://www.pythontutorial.net/python-oop/python-__new__/

from typing import TypeAlias, Union

IntOrFloat: TypeAlias = Union[int, float]


class A:

    def __init__(self):
        print(f"init of {self.__class__.__name__}")


class B:

    def __new__(cls, *args, **kwargs):
        print(f"new of {cls.__name__}")

    def __init__(self):
        print(f"init of {self.__class__.__name__}")


class Point2d:

    def __new__(cls, *args, **kwargs):
        print(f"inside __new__ of {cls.__name__}")
        print(f"{args=}")
        print(f"{kwargs=}")
        obj = object.__new__(cls)
        obj.x = float(kwargs["x"])
        return obj

    def __init__(self, x: IntOrFloat, y: IntOrFloat):
        print(f"inside __init__ of {self.__class__.__name__}")
        # self._x: float = float(x)
        self.y: float = float(y)

    def __str__(self):
        return


if __name__ == "__main__":
    a = A()
    b = B()

    p = Point2d(x=123, y=2.3)

    p2 = Point2d.__new__(Point2d, x=12, y=32)
    print(f"{p2.__dict__=}")

    p2.__init__(x=22, y=21)
    print(f"{p2.__dict__=}")
