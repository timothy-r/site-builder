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
        self._processed_pages = []

    # def process(self) -> None:
    #     self._process_page(
    #         source_path=self._root_page,
    #         site_path='index.html'
    #     )

    # def _process_page(self, source_path:str, site_path:str) -> None:
    #     """
    #         read page into a Page instance
    #         need to update Page - may be better to create a separate class & refactor common code
    #             * only need some linked files - eg not breadcrumbs

    #     """
    #     if not os.path.exists(source_path):
    #         # print("Source path does not exist: {}".format(source_path))
    #         return

    #     if source_path in self._processed_pages:
    #         """
    #             don't process pages twice
    #         """
    #         return

    #     print("ExtractionService: Processing page {}".format(source_path))

    #     try:

    #         with open(source_path, mode="r", encoding='utf-8') as f:
    #             html = f.read()

    #             page = Page(source_path=source_path, html=html, site_path=site_path)

    #             # specific to this class
    #             self._do_page_processing(page=page)

    #             pages = page.get_pages()

    #             # page_site_dir = os.path.dirname(site_path)

    #             self._processed_pages.append(source_path)

    #             for key in pages.keys():

    #                 print("Extracted page {} from {}".format(pages[key], source_path))

    #                 # sub_site_path = os.path.join(page_site_dir, key)
    #                 self._process_page(source_path=pages[key], site_path=key)

    #     except Exception as e:
    #         print ("ERROR processing {} : {}".format(source_path, e))

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