import unittest
import mockfs


from site_gen.node.linked_file import LinkedFile

class LinkedFileTest(unittest.TestCase):

    def setUp(self) -> None:
        super().setUp()
        self._mfs = mockfs.replace_builtins()
        self._root_path = '/opt/test/source'

        self._mfs.add_entries({self._root_path : ''})

    def tearDown(self) -> None:
        super().tearDown()
        mockfs.restore_builtins()

    def test_not_exists(self) -> None:

        link_path = 'test.html'
        source_path = self._root_path + "/test.html"
        parent_path = 'test.html'
        file = LinkedFile(link_path=link_path, system_path=source_path, host_page_path=parent_path)

        self.assertFalse(file.exists)

    def test_exists(self) -> None:

        file = self._create_mock_linked_file()

        self.assertTrue(file.exists)

    def test_is_html_file(self) -> None:

        file = self._create_mock_linked_file()

        self.assertTrue(file.is_html_file)
        self.assertFalse(file.is_media_file)

    def test_is_not_html_file(self) -> None:

        file = self._create_mock_linked_file(
            link_path='image.png',
            source_path='/image.png',
            parent_path='image.png'
        )
        self.assertFalse(file.is_html_file)
        self.assertTrue(file.is_media_file)

    def test_is_index_page(self) -> None:
        file = self._create_mock_linked_file(
            link_path='index.html',
            source_path='/index.html',
            parent_path='index.html'
        )

        self.assertTrue(file.is_index_file)

    def test_is_not_index_page(self) -> None:
        file = self._create_mock_linked_file(
            link_path='../../d/343/image.png',
            source_path='/d/343/image.png',
            parent_path='../../content.html'
        )

        self.assertFalse(file.is_index_file)


    def test_file_system_path(self) -> None:
        file = self._create_mock_linked_file(
            link_path='../../d/343/image.png',
            source_path='/d/343/image.png',
            parent_path='../../content.html'
        )
        file_system_path = file.file_system_path
        self.assertEqual(self._root_path + "/d/343/image.png", file_system_path)

    def test_site_file_path(self) -> None:
        file = self._create_mock_linked_file(
            link_path='../../d/343/image.png',
            source_path='/d/343/image.png',
            parent_path='/dir/pages/content.html'
        )
        site_file_path = file.host_page_path
        self.assertEqual('/d/343/image.png', site_file_path)

    # def test_rename_paths(self) -> None:
    #     pass

    def _create_mock_linked_file(
        self,
        link_path:str='index.html',
        source_path:str='/index.html',
        parent_path:str='index.html'
    ) -> LinkedFile:

        self._add_mock_file(path=source_path)

        file_source_path = self._root_path + source_path
        file = LinkedFile(link_path=link_path, system_path=file_source_path, host_page_path=parent_path)
        return file



    def _add_mock_file(self, path:str, contents:str = '') -> None:
        full_path = self._root_path + path
        self._mfs.add_entries({
            full_path: contents
        })

    def _add_mock_directory(self, path:str) -> None:
        data_path = self._root_path + '/' + path + '/index.yml'
        data = self._get_test_data_file_contents()
        self._mfs.add_entries({
            data_path: data
        })

    def _add_mock_root_directory(self) -> None:
        # add the index.yml file contents
        root_data_path = self._root_path + '/index.yml'
        root_data = self._get_test_root_data_file_contents()
        self._mfs.add_entries({
            root_data_path: root_data
            })

        self._add_mock_file('/css/inline_styles.css')
        self._add_mock_file('/js/inline_scripts.js')

    def _get_test_root_data_file_contents(self) -> str:
        return """
index:
    title: "My site"
common:
    owner:
        name: "My site owner"
        email: "My email"
    css:
        inline: css/inline_styles.css
    js:
        inline: js/inline_scripts.js
    """

    def _get_test_data_file_contents(self) -> str:
        return """
index:
    title: "Folder One"
    thumb: "thumb.png"
    sub_heading: "Folder one is the best folder"
contents:
    funky_foto:
      type: "img"
      title: "Funky Foto"
      src:
        file: "funky.png"
        height: 576
        width: 1024
    blog_post:
      type: "txt"
      title: "Blog Post"
      src:
        file: "blog_post.txt"
    cool_vid:
      type: "video"
      title: "Cool Video"
      src:
        file: "cool_video.mp4"
        height: 576
        width: 1024
"""