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
        site_path = 'test.html'
        file = LinkedFile(link_path=link_path, source_path=source_path, site_path=site_path)

        self.assertFalse(file.exists)

    def test_exists(self) -> None:

        link_path = 'test.html'
        source_path = self._root_path + "/test.html"
        site_path = 'test.html'

        self._add_mock_file(path='/test.html')

        file = LinkedFile(link_path=link_path, source_path=source_path, site_path=site_path)

        self.assertTrue(file.exists)

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