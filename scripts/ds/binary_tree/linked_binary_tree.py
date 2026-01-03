from scripts.ds.binary_tree.binary_tree_abc import BinaryTreeABC
from scripts.ds.binary_tree.position import Position
from scripts.ds.binary_tree.node import Node


class LinkedBinaryTree(BinaryTreeABC):

    def _validate(self, p: Position) -> Node | None:
        if isinstance(p, Position):
            raise Exception("Not instance of Position class")
        if p.container is not self:
            raise Exception("Not member of this tree")
        if p.node.parent is p.node:
            raise Exception("Deprecated node! ")
        return p.node

    def _make_position(self, node: Node | None) -> Position:
        return (
            Position(container=self, node=node)
            if node is not None else None
        )

    def __init__(self):
        pass