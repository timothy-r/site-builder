import os
import shutil

from site_gen.node.page import Page
from site_gen.process.process_service import ProcessService


"""
    Generates the data files for a static site
    Updates the source contents, cleans up names etc
"""
class ExtractionService(ProcessService):

    def __init__(self, root_page:str, target_dir:str) -> None:
        self._root_page = root_page
        self._target_dir = target_dir

    def _do_page_processing(self, page:Page) -> None:
        """
        switch behaviour on type of page
        index page
            process each sub folder
            create the file system folder
            generate the data.yml file with index data
            move the thumbnail images

        leaf page
            extract contents
            update data.yml
            move source files
        """
        if page.is_index_file:
            print("Processing index page {}".format(page))
            albums = page.get_albums()
            for album in albums:
                print("Processing album: {}".format(album.index_page.file_system_path))
        else:
            print("Processing content page {}".format(page))