# References:
# (1) https://www.geeksforgeeks.org/monkey-patching-in-python-dynamic-behavior/

from functools import partialmethod
from inspect import signature


class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y


if __name__ == "__main__":

    def my_getter(self, name):
        return getattr(self, name)

    Point2D.get_x = partialmethod(my_getter, name="x")
    Point2D.get_y = partialmethod(my_getter, name="y")
    print(f"{signature(Point2D.get_x)=}")

    p = Point2D(1, 3)
    print(f"{p.get_x()=}")
    print(f"{p.get_y()=}")

    # COMMENT: note that functools.partialmethod has to be used to create
    # a method capable of handling self; using functools.partialmethod will not
    # do the trick!
