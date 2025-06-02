from typing import Literal, overload, TypeAlias, Union
import random

Numeric: TypeAlias = Union[int, float]


@overload
def myfun(x: Literal[True]) -> int: ...


@overload
def myfun(x: Literal[False]) -> float: ...


def myfun(x: Literal[False, True]) -> Numeric:
    num: float = random.random()
    if x:
        return int(round(num, ndigits=0))
    return num


if __name__ == "__main__":
    print(f"{myfun(x=True)=}")
    print(f"{myfun(x=False)=}")
