import os
import shutil

from site_gen.node.page import Page
from site_gen.process.process_service import ProcessService

class CleanSourceService(ProcessService):

    def __init__(self, root_page:str, target_dir:str) -> None:

        self._root_page = root_page
        self._target_dir = target_dir

    def _do_page_processing(self, page:Page) -> None:
        self._write_html_page(page = page) #relative_path=site_path, html=page.get_html())

        files = page.get_files()
        for key in files.keys():
            self._copy_file(relative_path=key, source_path=files[key])

    def _write_html_page(self, page:Page) -> None:

        target_path = os.path.abspath(
            os.path.join(self._target_dir, page.site_path)
        )

        self._ensure_directory_exists(path=target_path)

        if not os.path.exists(target_path):
            print("Write html page {}".format(target_path))
            with open(target_path, mode='w', encoding='utf-8') as f:
                f.write(page.get_html())

    def _copy_file(self, relative_path:str, source_path:str) -> None:

        target_path = os.path.abspath(
            os.path.join(self._target_dir, relative_path)
        )
        self._ensure_directory_exists(path=target_path)

        if not os.path.exists(target_path):
            # print("Copy file from {} to {}".format(source_path, target_path))
            shutil.copy(source_path, target_path)


