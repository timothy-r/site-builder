import unittest
import mockfs
from bs4 import BeautifulSoup, Tag


from site_gen.node.page import Page

class PageTest(unittest.TestCase):

    def test_is_index_file(self) -> None:
        page = Page(system_path='/opt/test/source/index.html', html='', site_path='index.html')

        self.assertTrue(page.is_index_file)

    def test_is_not_index_file(self) -> None:
        page = Page(system_path='/opt/test/source/images/funky.png', html='', site_path='images/funky.png')

        self.assertFalse(page.is_index_file)

    def test_get_albums(self) -> None:
        album_count = 1
        html = self._get_index_html(albums=album_count)
        page = Page(system_path='/opt/test/source/index.html', html=html, site_path='index.html')

        albums = page.get_albums()
        self.assertEqual(album_count, len(albums))

    def test_get_leaf_albums(self) -> None:
        album_count = 3
        html = self._get_leaf_page_index_html(albums=album_count)

        page = Page(system_path='/opt/test/source/graphics/index.html', html=html, site_path='graphics/index.html')
        albums = page.get_albums()

        self.assertEqual(album_count, len(albums))

    # def test_get_mixed_albums(self) -> None:
    #     album_count = 4
    #     html = self._get_mixed_index_html(albums=album_count)

    #     page = Page(system_path='/opt/test/source/graphics/index.html', html=html, site_path='graphics/index.html')
    #     albums = page.get_albums()

    #     self.assertEqual(album_count, len(albums))


    def test_get_albums_from_non_index_page(self) -> None:
        album_count = 0
        page = Page(system_path='/opt/test/source/page.html', html='', site_path='page.html')

        albums = page.get_albums()
        self.assertEqual(album_count, len(albums))


    def _get_index_html(self, albums=4) -> str:

        html = '<html>'
        html += '<body class="gallery">'
        html += '<div id="gallery">'
        html += '<div class="content">'
        html += '<h2>Test Site</h2>'
        html += '<div class="gallery-albums">'

        for a in range(0, albums):
            html += '<div class="gallery-album"><div class="gallery-thumb">'
            html += '<a href="v/album_{}/index.html">'.format(a)
            html += '<img alt="Album {}" height="80" src="d/123{}/thumbnail.png" width="100"/>'.format(a, a)
            html += '</a></div>'
            html += '<h4><a href="v/album_{}/index.html">Album {}</a></h4>'.format(a,a)
            html += '<div class="meta">{} images</div>'.format(albums)
            html += '<p>Album {}</p>'.format(a)
            html += '</div>'

        html += '</div></div></div>'
        html += '</body></html>'

        dom_doc = BeautifulSoup(html, 'html.parser')

        return dom_doc.prettify()

    def _get_leaf_page_index_html(self, albums=4) -> str:

        html = '<html>'
        html += '<body class="gallery">'
        html += '<div id="gallery">'
        html += '<div class="content">'
        html += '<h2>Test Site</h2>'
        html += '<div class="gallery-items">'

        for a in range(0, albums):
            html += '<div class="gallery-thumb">'
            html += '<a href="v/album_{}/index.html">'.format(a)
            html += '<img alt="Album {}" height="80" src="d/123{}/thumbnail.png" width="100"/>'.format(a, a)
            html += '</a></div>'

        html += '</div></div></div>'
        html += '</body></html>'

        dom_doc = BeautifulSoup(html, 'html.parser')

        return dom_doc.prettify()

    def _get_mixed_index_html(self, albums:int=1, leaf_albums:int=1) -> str:
        html = '<html>'
        html += '<body class="gallery">'
        html += '<div id="gallery">'
        html += '<div class="content">'
        html += '<h2>Test Site</h2>'

        html += '<div class="gallery-albums">'

        for a in range(0, albums):
            html += '<div class="gallery-album"><div class="gallery-thumb">'
            html += '<a href="v/album_{}/index.html">'.format(a)
            html += '<img alt="Album {}" height="80" src="d/123{}/thumbnail.png" width="100"/>'.format(a, a)
            html += '</a></div>'
            html += '<h4><a href="v/album_{}/index.html">Album {}</a></h4>'.format(a,a)
            html += '<div class="meta">{} images</div>'.format(albums)
            html += '<p>Album {}</p>'.format(a)
            html += '</div>'

        html += '</div></div></div>'
        html += '</body></html>'

        dom_doc = BeautifulSoup(html, 'html.parser')
