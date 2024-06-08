from string import ascii_uppercase
from typing import Any, TypeAlias

from loguru import logger

List: TypeAlias = list[Any]


class ListContainer:

    def __init__(self, values: List):
        self._values: List = values

    def __rshift__(self, other) -> str:
        logger.info(f"{other=}")
        if len(self._values) <= other:
            return ""
        return "".join(self._values[other:])

    def __lshift__(self, other) -> str:
        logger.info(f"{other=}")
        if len(self._values) <= other:
            return ""
        return "".join(self._values[:len(self._values)-other])

    def __str__(self):
        return "".join(self._values)


if __name__ == "__main__":

    lc = ListContainer(values=list(ascii_uppercase))

    print(lc)
    print(lc >> 10)
    print(lc << 10)
