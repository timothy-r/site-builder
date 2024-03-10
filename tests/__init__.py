"""
    test module
"""
import unittest

from tests.album_test import AlbumTest
from tests.linked_file_test import LinkedFileTest
from tests.page_test import PageTest
from tests.node_test import NodeTest

from tests.node_tree_generator_test import NodeTreeGeneratorTest

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    suite = unittest.TestSuite()

    runner.run(suite)