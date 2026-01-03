from __future__ import annotations
from typing import Optional

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
        self._root: Optional[Node] = None
        self._size: int = 0

    def __len__(self) -> int:
        return self._size

    def root(self) -> Position:
        return self._make_position(node=self._root)

    def parent(self, p: Position) -> Position | None:
        node = self._validate(p=p)
        return self._make_position(node=node)

    def left(self, p: Position) -> Position | None:
        node = self._validate(p=p)
        return self._make_position(node=node.left)

    def right(self, p: Position) -> Position | None:
        node = self._validate(p=p)
        return self._make_position(node=node.right)

    def num_children(self, p: Position):
        node = self._validate(p=p)
        ch_count = 0
        if node.left is not None:
            ch_count += 1
        if node.right is not None:
            ch_count += 1
        return ch_count

    def _add_root(self, elem: int):
        if self._root is not None:
            raise Exception("Root is already set!")
        self._size = 1
        self._root = Node(element=elem)
        return self._make_position(node=self._root)

    def _add_left(self, p: Position, elem: int) -> Position:
        node = self._validate(p=p)
        if node.left is not None:
            raise Exception(
                f"Cannot add the left child; "
                f"Left child of node {node.element} is not none!"
            )
        node.left = Node(element=elem, parent=node)
        self._size += 1
        return self._make_position(node=node.left)

    def _add_right(self, p: Position, elem: int) -> Position:
        node = self._validate(p=p)
        if node.right is not None:
            raise Exception(
                f"Cannot add the right child; "
                f"Right child of node {node.element} is not none!"
            )
        node.right = Node(element=elem, parent=node)
        self._size += 1
        return self._make_position(node=node.right)

    def _replace(self, p: Position, elem: int) -> int | None:
        node = self._validate(p=p)
        old_elem = node.element
        node.element = elem
        return old_elem

    def _delete(self, p: Position) -> int | None:
        node = self._validate(p=p)
        if self.num_children(p=p) == 2:
            raise Exception("Node to be removed has 2 children! cannot remove!")
        only_child: Node = node.left if node.left is not None else node.right

        if self.is_root(p=p):
            self._root = only_child
        else:
            node_parent = node.parent
            if node is node_parent.left:
                node_parent.left = only_child
            else:
                node_parent.right = only_child
        self._size -= 1
        node.parent = node # deprecate the deleted node
        return node.element

    def _attach(
            self,
            p: Position,
            tl: Optional[LinkedBinaryTree],
            tr: Optional[LinkedBinaryTree]
    ):
        node = self._validate(p=p)
        if not self.is_leaf(p=p):
            raise Exception("Cannot attach to non-leaf! ")
        self._size = self._size + len(tl) + len(tr)
        if not tl.is_empty():
            node.left = tl.root
            tl.root.parent = node
            tl.root = None
            tl._size = 0
        if not tr.is_empty():
            node.right = tr.root
            tr.root.parent = node
            tr.root = None
            tr._size = 0
