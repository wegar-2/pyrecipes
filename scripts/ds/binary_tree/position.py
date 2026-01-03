from scripts.ds.binary_tree.position_abc import PositionABC
from scripts.ds.binary_tree.binary_tree_abc import BinaryTreeABC
from scripts.ds.binary_tree.node import Node

__all__ = ["Position"]


class Position(PositionABC):

    def __init__(self, container: BinaryTreeABC, node: Node):
        self._container: BinaryTreeABC = container
        self._node: Node = node

    @property
    def element(self) -> int:
        return self._node.element

    @property
    def node(self):
        return self._node

    @property
    def container(self):
        return self._container

    @property
    def parent(self) -> Node:
        return self._node.parent
