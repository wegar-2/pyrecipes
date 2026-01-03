from abc import ABC, abstractmethod
from scripts.ds.binary_tree.tree_abc import TreeABC
from scripts.ds.binary_tree.position_abc import PositionABC


class BinaryTreeABC(ABC, TreeABC):

    def __init__(self, root):
        self._root = root

    @abstractmethod
    def left(self, p: PositionABC):
        pass

    @abstractmethod
    def right(self, p: PositionABC):
        pass

    def sibling(self, p: PositionABC):
        parent = p.parent
        if parent is None:
            return None
        if self == self.left(p=parent):
            if (sibling := self.right(p=parent)) is not None:
                return sibling
            return None
        else:
            if (sibling := self.left(p=parent)) is not None:
                return sibling
            return None

    def children(self, p: PositionABC):
        if (left_child := self.left(p=p)) is not None:
            yield left_child
        if (right_child := self.right(p=p)) is not None:
            yield right_child
