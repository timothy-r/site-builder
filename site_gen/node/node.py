
"""
    a node in a tree of pages in a site
"""
class Node:

    def __init__(self, source_file:str) -> None:
        self._source_file = source_file
        self._parent = None
        self._children = set()

    @property
    def source_file(self) -> str:
        return self._source_file

    @property
    def title(self) -> str:
        pass

    def add_child(self, node:"Node") -> None:
        if node in self._children:
            return

        if node.parent:
            node.parent.remove_child(node=node)
        self._children.add(node)
        node._parent = self

    def remove_child(self, node:"Node") -> None:
        self._children.remove(node)
        node._parent = None

    @property
    def children(self) -> list["Node"]:
        return list(self._children)

    @property
    def parent(self) -> "Node":
        return self._parent
