import unittest

from site_gen.generator.node_tree_generator import NodeTreeGenerator
from site_gen.node.node import Node

class NodeTreeGeneratorTest(unittest.TestCase):

    def test_generate(self) -> None:

        generator = NodeTreeGenerator(node_factory=node_factory)
        source_file = 'index.html'
        node = generator.generate(source_file=source_file)

        self.assertIsInstance(node, Node)
        self.assertEqual(source_file, node.source_file)

def node_factory(source_file:str) -> Node:

    return Node(source_file=source_file)