from abc import ABC, abstractmethod
import os
import logging

from site_gen.node.page import Page

"""
    Implements the processing of a set of linked resources (pages or data)
"""
class ProcessService(ABC):

    def __init__(self, root_page:str, target_dir:str) -> None:
        super().__init__()
        self._root_page = root_page
        self._target_dir = target_dir

    def process(self) -> None:

        self._processed_pages = []

        self._process_page(
            source_path=self._root_page,
            site_path='index.html'
        )

    @abstractmethod
    def _do_page_processing(self, page:Page) -> None:
        pass

    def _process_page(self, source_path:str, site_path:str) -> None:
        """
            read page into a Page instance
            need to update Page - may be better to create a separate class & refactor common code
                * only need some linked files - eg not breadcrumbs

        """
        if not os.path.exists(source_path):
            # logging.info("Source path does not exist: {}".format(source_path))
            return

        if source_path in self._processed_pages:
            """
                don't process pages twice
            """
            return

        logging.info("{}: Processing page {}".format(__class__.__name__, source_path))

        try:

            with open(source_path, mode="r", encoding='utf-8') as f:
                html = f.read()

                page = Page(system_path=source_path, html=html, site_path=site_path)

                # specific to this class
                self._do_page_processing(page=page)

                pages = page.get_pages()

                # page_site_dir = os.path.dirname(site_path)

                self._processed_pages.append(source_path)

                for key in pages.keys():

                    # logging.info("Extracted page {} from {}".format(pages[key], source_path))

                    # sub_site_path = os.path.join(page_site_dir, key)
                    self._process_page(source_path=pages[key], site_path=key)

        except Exception as e:
            logging.exception("{} processing {} : {}".format(__class__.__name__, source_path, e))


    def _ensure_directory_exists(self, path:str) -> None:
        location = os.path.dirname(path)
        try:
            os.makedirs(name=location, exist_ok=True)
        except FileExistsError as error:
            logging.error("_ensure_directory_exists failed {}".format(error))