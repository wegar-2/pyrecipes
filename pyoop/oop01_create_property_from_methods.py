from typing import TypeAlias, Union

Numeric: TypeAlias = Union[float, int]


class Point1d:

    def __init__(self, x: Numeric):
        self._x: float = float(x)

    def get_x(self) -> float:
        return self._x

    def set_x(self, x):
        self._x = float(x)

    x = property(
        fget=get_x,  # noqa
        fset=set_x,  # noqa
    )


if __name__ == "__main__":

    p = Point1d(1)
    print(f"{p.x=}")
    p.x = 32
    print(f"{p.x=}")
