from typing import overload, Optional
import math


@overload
def norm(x: float, y: float) -> float:
    pass


@overload
def norm(x: float, y: float, z: float) -> float:
    pass


def norm(x: float, y: float, z: Optional[float] = None):
    if z is None:
        return math.sqrt(math.pow(x, 2) + math.pow(y, 2))
    else:
        return math.sqrt(math.pow(x, 2) + math.pow(y, 2) + math.pow(z, 2))


if __name__ == "__main__":
    print(f"{norm(x=12, y=3)=}")
    print(f"{norm(x=12, y=3, z=22)=}")
