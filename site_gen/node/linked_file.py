import pathlib
import os
import re

"""
    encapsulate a system file, its site path and its link path in a HTML document
"""
class LinkedFile:

    def __init__(self, link_path:str, system_path:str, host_page_path:str) -> None:
        """
            link_path: the path embeded in the HTML doc to this file
            system_path: the file system path of page this file was extracted from
            host_page_path: the path to the page in the site that this file was linked from
        """
        self._link_path = link_path
        self._system_path = system_path
        self._host_page_path = host_page_path

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

        source_location = os.path.dirname(self._system_path)
        return os.path.normpath(os.path.join(source_location, self._link_path))

    @property
    def file_system_path_normalised(self) -> str:
        # site_file_path
        return self._normalise_string(self.file_system_path)

    @property
    def host_page_path(self) -> str:

        site_location = os.path.dirname(self._host_page_path)
        return os.path.normpath(os.path.join(site_location, self._link_path))

    @property
    def host_page_path_normalised(self) -> str:
        # site_file_path
        return self._normalise_string(self.host_page_path)

    @property
    def base_name(self) -> str:
        parts = os.path.split(os.path.dirname(self._link_path))
        return parts[-1]

    @property
    def base_name_normalised(self) -> str:
        # site_file_path
        return self._normalise_string(self.base_name)

    @property
    def file_name_normalised(self) -> str:
        name = os.path.basename(self._link_path)
        return self._normalise_string(name=name)

    def __repr__(self) -> str:
        return "LinkedFile(link_path='{}', system_path='{}', host_page_path='{}')".format(
            self._link_path,
            self._system_path,
            self._host_page_path
        )

    def _normalise_string(self, name:str) -> str:

        name = re.sub(pattern='^v/',repl='',string=name)
        name = re.sub(pattern='^d/',repl='',string=name)

        name = name.lower()
        name = name.replace('+','_')
        name = name.replace('-', '_')
        return name