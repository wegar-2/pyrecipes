from functools import partial
from typing import Any, Type
import random


class MetaPoint(type):

    def __new__(mcls, name, bases, class_dict, **kwargs) -> Type:
        new_cls: Type = super().__new__(mcls, name, bases, class_dict)

        try:
            dim = kwargs["dim"]
        except KeyError:
            print("No dimension passed; defaulting to Cartesian")
            dim = 3

        for k in range(1, dim+1, 1):
            print(f"Setting x{k} methods...")
            setattr(new_cls, f"get_x{k}", lambda self: getattr(self, f"x{k}"))
            setattr(new_cls, f"set_x{k}", lambda self, value: setattr(self, f"x{k}", value))

        return new_cls


class MyPoint(metaclass=MetaPoint, dim=10):

    def __init__(self):
        for k in range(1, 11, 1):
            setattr(self, f"x{k}", random.uniform(0, 1))


if __name__ == "__main__":
    p = MyPoint()
    print(f"{getattr(p, 'get_x1')()=}")
