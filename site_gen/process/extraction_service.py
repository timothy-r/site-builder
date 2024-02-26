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

    def process(self) -> None:
        print("Not implemented")
        self._process_page(
            source_path=self._root_page,
            site_path='index.html'
        )

    def _process_page(self, source_path:str, site_path:str) -> None:
        """
            read page into a Page instance
            need to update Page - may be better to create a separate class & refactor common code
                * only need some linked files - eg not breadcrumbs

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