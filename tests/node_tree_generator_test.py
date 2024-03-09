import unittest

from site_gen.generator.node_tree_generator import NodeTreeGenerator
from site_gen.node.node import Node

class NodeTreeGeneratorTest(unittest.TestCase):

    def test_generate(self) -> None:

        generator = NodeTreeGenerator()
        source_file = ''
        node = generator.generate(source_file=source_file)

        self.assertIsInstance(node, Node)