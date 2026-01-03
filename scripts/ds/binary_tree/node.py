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

    @property
    def parent(self) -> Node:
        return self._parent

