from __future__ import annotations
from typing import Final

import numpy as np
from loguru import logger


class MyMetaclass(type):

    @staticmethod
    def _get_random_salt():
        return int(np.random.randint(0, 1_000_000_000, size=1)[0])

    def __call__(cls, *args, **kwargs):

        # check if class being created has member instances of type dict;
        # if it does not, add it
        if not hasattr(cls, "instances"):
            cls.instances = {}

        temp_instance = super().__call__(*args, **kwargs)

        for k, v in cls.instances.items():
            if v == temp_instance:
                logger.info("Object already exists; "
                            "returning the existing instance")
                return v

        temp_instance_hash: int = hash(temp_instance)
        if temp_instance_hash in cls.instances:
            logger.warning("ENCOUNTERED HASH COLLISION! Setting random salt ")
            kwargs["salt"] = cls._get_random_salt()
            new_instance = super().__call__(*args, **kwargs)
            new_instance_hash: int = hash(new_instance)
            if new_instance_hash in cls.instances:
                raise ValueError("Repeated hash collision encountered! "
                                 "This situation is a total outlier! ")
            cls.instances[new_instance_hash] = new_instance
            return new_instance

        cls.instances[temp_instance_hash] = temp_instance
        return temp_instance


class MyPoint(metaclass=MyMetaclass):

    def __init__(self, x: int, y: int, salt: int = 0):
        self._x: int = x
        self._y: int = y
        self._salt: int = salt

    @property
    def x(self) -> int:
        return self._x

    @property
    def y(self) -> int:
        return self._y

    def __hash__(self):
        return self._x + self._y + self._salt
        # return hash((self._x, self._y))

    def __eq__(self, other: MyPoint) -> bool:
        return (self._x == other.x) & (self._y == other.y)


if __name__ == "__main__":

    p1 = MyPoint(10, 3)
    print(MyPoint.instances)

    p2 = MyPoint(6, 7)
    print(MyPoint.instances)

    p3 = MyPoint(10, 3)
    print(MyPoint.instances)

    print(MyPoint.instances)

    print("done!")
