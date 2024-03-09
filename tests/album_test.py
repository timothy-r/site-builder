import unittest


from site_gen.node.album import Album
from site_gen.node.node_type import NodeType
from site_gen.node.linked_file import LinkedFile

class AlbumTest(unittest.TestCase):

    def test_album(self) -> None:
        page = LinkedFile(link_path='index.html', system_path='/index.html', host_page_path='index.html')
        thumbnail = LinkedFile(link_path='/d/images/xxx/thumb.png',system_path='/d/images/xxx/thumb.png', host_page_path='index.html')
        title = 'album'

        album = Album(
            index_page=page,
            title=title,
            type=NodeType.DIRECTORY,
            source_page='index.html',
            thumbnail=thumbnail,
            thumbnail_height=100,
            thumbnail_width=100
        )

        self.assertIsInstance(album, Album)

    # def test_rename_file_paths(self) -> None:
    #     pass