import unittest

from site_gen.node.node import Node

class NodeTest(unittest.TestCase):

    def test_node(self) -> None:

        source_file = '/index.html'
        node = Node(source_file=source_file)

        self.assertIsInstance(node, Node)
        self.assertEqual(source_file, node.source_file)

    def test_node_add_child(self) -> None:
        parent_source_file = '/index.html'
        parent = Node(source_file=parent_source_file)

        child_source_file = '/dir/index.html'
        child = Node(
            source_file=child_source_file
        )

        self.assertIsNone(child.parent)

        parent.add_child(child)

        self.assertEqual(1, len(parent.children))
        self.assertEqual(parent, child.parent)
        self.assertTrue(child in parent.children)

        new_parent_source_file = '/new_index.html'
        new_parent = Node(source_file=new_parent_source_file)

        new_parent.add_child(child)

        self.assertEqual(0, len(parent.children))
        self.assertEqual(1, len(new_parent.children))
        self.assertEqual(new_parent, child.parent)
        self.assertTrue(child in new_parent.children)
