from typing import Callable

from site_gen.node.node import Node

"""
    from a source file generates a tree of Nodes
"""
class NodeTreeGenerator:

    def __init__(self, node_factory:Callable) -> None:
        self._node_factory = node_factory

    def generate(self, source_file:str) -> Node:
        node = self._node_factory(source_file)

        return node

    def _process_node(self, node:Node) -> None:
        pass
