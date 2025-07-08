import inspect
from types import FunctionType, MethodType
from typing import Any


def log_function():
    """Function for logging another function call"""
    print(f"Inside {inspect.stack()[1].function} function...")


def just_a_function(x=1):
    log_function()
    print(f"{x=}")


def log_method(x: Any) -> None:
    """Function for logging class method call"""
    print(f"Inside method {inspect.stack()[1].function} of class "
          f"{x.__class__.__name__}")


class Point2d:
    """Boring class"""

    def __init__(self):
        self.x = 123
        self.y = 321

    def set_x(self, x):
        log_method(x=self)
        self.x = x


if __name__ == "__main__":

    just_a_function()
    print(f"{isinstance(just_a_function, FunctionType)=}")
    print("\n")

    p = Point2d()
    p.set_x(333)
