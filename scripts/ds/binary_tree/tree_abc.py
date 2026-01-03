from abc import ABC, abstractmethod

from scripts.ds.binary_tree.position_abc import PositionABC


class TreeABC(ABC):

    @abstractmethod
    @property
    def root(self):
        pass

    @abstractmethod
    def parent(self, p: PositionABC):
        pass

    @abstractmethod
    def num_children(self, p: PositionABC):
        pass

    @abstractmethod
    def children(self):
        pass

    @abstractmethod
    def __len__(self):
        pass

    def is_root(self, p: PositionABC):
        return self.root == p

    @abstractmethod
    def is_empty(self):
        return len(self) == 0

    @abstractmethod
    def is_leaf(self, p: PositionABC):
        return self.num_children(p=p) == 0
