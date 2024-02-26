import unittest
import mockfs


from site_gen.node.page import Page

class PageTest(unittest.TestCase):

    def test_is_index_file(self) -> None:
        page = Page(source_path='/opt/source/test/index.html', html='', site_path='index.html')

        self.assertTrue(page.is_index_file)

    def test_is_not_index_file(self) -> None:
        page = Page(source_path='/opt/source/test/images/funky.png', html='', site_path='images/funky.png')

        self.assertFalse(page.is_index_file)

    def test_get_albums(self) -> None:
        pass