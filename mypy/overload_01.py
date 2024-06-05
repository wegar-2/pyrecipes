from typing import overload, Optional
import math


@overload
def norm(x: float, y: float) -> float:
    return math.sqrt(math.pow(x, 2) + math.pow(y, 2))


@overload
def norm(x: float, y: float, z: float) -> float:
    return math.sqrt(math.pow(x, 2) + math.pow(y, 2) + math.pow(z, 2))


def norm(x: float, y: float, z: Optional[float] = None):
    if z is None:
        return norm(x=x, y=y)
    else:
        return norm(x=x, y=y, z=z)
    