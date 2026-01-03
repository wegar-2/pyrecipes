from __future__ import annotations
from typing import Optional


class Node:

    __slots__ = ("_element", "_parent", "_left", "_right")

    def __init__(
            self,
            element: int,
            parent: Optional[Node] = None,
            left: Optional[Node] = None,
            right: Optional[Node] = None
    ):
        self._element: int = element
        self._parent: Optional[Node] = parent
        self._left: Optional[Node] = left
        self._right: Optional[Node] = right

    @property
    def element(self) -> int:
        return self._element

    @element.setter
    def element(self, elem: int):
        self._element = elem

    @property
    def parent(self) -> Node | None:
        return self._parent

    @property
    def left(self) -> Node | None:
        return self._left

    @property
    def right(self) -> Node | None:
        return self._right
