import unittest
import mockfs
from bs4 import BeautifulSoup, Tag


from site_gen.node.page import Page
from site_gen.node.page_content import PageContent

class PageTest(unittest.TestCase):

    def test_is_index_file(self) -> None:
        page = Page(system_path='/opt/test/source/index.html', html='', site_path='index.html')

        self.assertTrue(page.is_index_file)

    def test_is_not_index_file(self) -> None:
        page = Page(system_path='/opt/test/source/images/funky.png', html='', site_path='images/funky.png')

        self.assertFalse(page.is_index_file)

    def test_get_albums(self) -> None:
        album_count = 1
        html = self._get_album_index_html(albums=album_count)
        page = Page(system_path='/opt/test/source/index.html', html=html, site_path='index.html')

        albums = page.get_albums()
        self.assertEqual(album_count, len(albums))

    def test_get_leaf_albums(self) -> None:
        album_count = 3
        html = self._get_leaf_page_index_html(albums=album_count)

        page = Page(system_path='/opt/test/source/graphics/index.html', html=html, site_path='graphics/index.html')
        albums = page.get_albums()

        self.assertEqual(album_count, len(albums))

    def test_get_mixed_albums(self) -> None:
        album_count = 4
        leaf_albums = 1

        html = self._get_mixed_index_html(albums=album_count, leaf_albums=leaf_albums)

        page = Page(system_path='/opt/test/source/graphics/index.html', html=html, site_path='graphics/index.html')
        albums = page.get_albums()

        self.assertEqual(album_count+leaf_albums, len(albums))

    def test_get_albums_from_non_index_page(self) -> None:
        album_count = 0
        page = Page(system_path='/opt/test/source/page.html', html='', site_path='page.html')

        albums = page.get_albums()
        self.assertEqual(album_count, len(albums))

    def test_get_content(self) -> None:

        title = 'content test'
        img = 'test.01.png'
        download_img = 'test.download.01.png'
        html = self._get_content_page(title=title, image=img, download_img=download_img)
        page = Page(system_path='/opt/test/source/page.html', html=html, site_path='page.html')
        content = page.get_content()
        self.assertIsInstance(content, PageContent)
        self.assertEqual(title, content.title)
        self.assertEqual(img, content.source.file_name_normalised)
        self.assertEqual(download_img, content.download_file.file_name_normalised)

    def _wrap_content_in_page_html(self, title:str='Test Page', content:str='') -> str:
        html = '<html>'
        html += '<head><title>{}</title></head>'.format(title)
        html += '<body class="gallery">'
        html += '<div id="gallery">'
        html += '<div class="content">'
        html += '<h2>{}</h2>'.format(title)

        html += content

        html += '</div></div>'
        html += '</body></html>'
        return html

    def _get_album_index_html(self, albums=4) -> str:

        html = '<div class="gallery-albums">'
        for a in range(0, albums):
            html += self._get_album_item_html(albums=albums, item=a)
        html += '</div>'

        html = self._wrap_content_in_page_html(content=html, title='Index Page')

        return BeautifulSoup(html, 'html.parser').prettify()

    def _get_leaf_page_index_html(self, albums=4) -> str:

        html = '<div class="gallery-items">'
        for leaf in range(0, albums):
            html += self._get_leaf_item_html(leaf=leaf)
        html += '</div>'

        html = self._wrap_content_in_page_html(title='Leaf Index Page', content=html)

        return BeautifulSoup(html, 'html.parser').prettify()

    def _get_mixed_index_html(self, albums:int=1, leaf_albums:int=1) -> str:

        html = '<div class="gallery-albums">'
        for a in range(0, albums):
            html += self._get_album_item_html(albums=albums, item=a)
        html += '</div>'

        html += '<div class="gallery-items">'
        for leaf in range(0, leaf_albums):
            html += self._get_leaf_item_html(leaf=leaf)
        html += '</div>'

        html = self._wrap_content_in_page_html(title='Mixed Index Page', content=html)

        return BeautifulSoup(html, 'html.parser').prettify()

    def _get_content_page(self, title:str, image:str, download_img:str) -> str:

        html = '<div class="gallery-photo">'
        html += '<img src="../../../../d/700-2/{}" width="800" height="640" class="gallery-photo" usemap="#prevnext" alt="{}"/>'.format(image, title)

        html += '<a href="{}.html" id="nextArrow" style="position:absolute; margin: 30px 0 0 -50px; visibility: hidden">'.format(image)
        html += '<img src="../../../../themes/noodle/images/arrow-right.gif" alt="" width="20" height="17"/>'
        html += '</a>'

        html += '</div>'
        html += '<p><a href="../../../../d/698-2/{}">Download photo(1160x928)</a></p>'.format(download_img)

        html = self._wrap_content_in_page_html(content=html, title=title)

        dom_doc = BeautifulSoup(html, 'html.parser')
        return dom_doc.prettify()

    def _get_album_item_html(self, albums:int, item:int) -> str:

        html = '<div class="gallery-album"><div class="gallery-thumb">'
        html += '<a href="v/album_{}/index.html">'.format(item)
        html += '<img alt="Album {}" height="80" src="d/123{}/thumbnail.png" width="100"/>'.format(item, item)
        html += '</a></div>'
        html += '<h4><a href="v/album_{}/index.html">Album {}</a></h4>'.format(item, item)
        html += '<div class="meta">{} images</div>'.format(albums)
        html += '<p>Album {}</p>'.format(item)
        html += '</div>'

        return html

    def _get_leaf_item_html(self, leaf:int) -> str:

        html = '<div class="gallery-thumb">'
        html += '<a href="v/album_{}/index.html">'.format(leaf)
        html += '<img alt="Album {}" height="80" src="d/123{}/thumbnail.png" width="100"/>'.format(leaf, leaf)
        html += '</a></div>'

        return html
