from types import FunctionType, MethodType
from typing import Any


def run_checks(x: Any) -> None:
    print(f"{x=}")
    print(f"{isinstance(x, FunctionType)=}")
    print(f"{isinstance(x, MethodType)=}")


def my_method(x, y):
    return x + y

class Point:
    def __init__(self):
        self.x = 1
        self.y = 2

    def print(self):
        print(f"Point(x={self.x}, y={self.y})")


if __name__ == "__main__":
    run_checks(x=123)
    run_checks(x=my_method)

    p = Point()
    run_checks(p)
    run_checks(p.print)
