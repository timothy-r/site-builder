import pathlib
import os

"""
    encapsulate a source file, its site path and its link path in a HTML document
"""
class LinkedFile:

    def __init__(self, link_path:str, source_path:str, parent_path:str) -> None:
        """
            link_path: the path embeded in the HTML doc to this file
            source_path: the path to the parent page file on the file system
            site_path: the path to the page in the site that this file was linked from
        """
        self._link_path = link_path
        self._source_path = source_path
        self._parent_path = parent_path

        self._exclude_list = [
            'http://gallery.sourceforge.net',
            'mailto:flo.richer',
            'main.php',
            'http://www.adobe.com/go/getflash'
        ]

        self._valid_html_extensions = ['.html']
        self._invalid_html_path_item = 'hiplc'

    @property
    def is_valid(self) -> bool:
        return not self._link_path in self._exclude_list

    @property
    def is_html_file(self) -> bool:
        if not self.is_valid:
            return False
        return self._test_html_file(path=self._link_path)

    @property
    def is_media_file(self) -> bool:
        if not self.is_valid:
            return False

        return not self._test_html_file(path=self._link_path)

    @property
    def is_index_file(self) -> bool:
        """
            is this an index page?
        """
        return pathlib.PurePath(self._link_path).name == 'index.html'

    def _test_html_file(self, path:str) -> bool:
        page_ext = pathlib.Path(path).suffix

        if page_ext in self._valid_html_extensions:
            parts = pathlib.PurePath(path).name.split('.')
            if self._invalid_html_path_item in parts:
                return False
            else:
                return True
        else:
            return False

    @property
    def exists(self) -> bool:
        return os.path.exists(
            self.file_system_path
        )

    @property
    def file_system_path(self) -> str:

        source_location = os.path.dirname(self._source_path)
        return os.path.normpath(os.path.join(source_location, self._link_path))

    @property
    def site_file_path(self) -> str:

        site_location = os.path.dirname(self._parent_path)
        return os.path.normpath(os.path.join(site_location, self._link_path))

    def rename_paths(self) ->  None:
        """
            rename the file paths
        """

    def __repr__(self) -> str:
        return "LinkedFile(link_path='{}', source_path='{}', parent_path='{}')".format(
            self._link_path,
            self._source_path,
            self._parent_path
        )