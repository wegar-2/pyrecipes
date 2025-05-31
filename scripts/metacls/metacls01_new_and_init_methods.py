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


if __name__ == "__main__":
    a = A()
    b = B()

    p = Point2d(x=123, y=2.3)

    p2 = Point2d.__new__(Point2d, x=12, y=32)
    print(f"{p2.__dict__=}")

    p2.__init__(x=22, y=21)
    print(f"{p2.__dict__=}")

    # Output:
    #
    # init of A
    # new of B
    # inside __new__ of Point2d
    # args=()
    # kwargs={'x': 123, 'y': 2.3}
    # inside __init__ of Point2d
    # inside __new__ of Point2d
    # args=()
    # kwargs={'x': 12, 'y': 32}
    # p2.__dict__={'x': 12.0}
    # inside __init__ of Point2d
    # p2.__dict__={'x': 12.0, 'y': 21.0}
    #
    #  COMMENT: note what the output of p2.__dict__ calls are in two cases:
    #       (1) after calling __new__ only
    #       (2) after calling both: __new__ and __init__
    #
    # COMMENT 2: keep in mind that the first argument of the __new__ method
    #       is class not an instance
