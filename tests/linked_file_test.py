import unittest
import mockfs


from site_gen.node.linked_file import LinkedFile

class LinkedFileTest(unittest.TestCase):

    def test_exists(self) -> None:
        # self.assertTrue(False)
        file = LinkedFile(link_path='', source_page_path='', site_path='')
        self.assertFalse(file.exists)
