import unittest


from site_gen.node.album import Album
from site_gen.node.linked_file import LinkedFile

class AlbumTest(unittest.TestCase):

    def test_album(self) -> None:
        page = LinkedFile(link_path='index.html', source_path='/index.html', parent_path='index.html')
        thumbnail = LinkedFile(link_path='/d/images/xxx/thumb.png',source_path='/d/images/xxx/thumb.png', parent_path='index.html')
        title = 'album'

        album = Album(
            index_page=page,
            title=title,
            thumbnail=thumbnail,
            thumbnail_height=100,
            thumbnail_width=100
        )

        self.assertIsInstance(album, Album)