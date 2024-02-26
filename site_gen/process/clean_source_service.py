import os
import shutil

from site_gen.node.page import Page
from site_gen.process.process_service import ProcessService

class CleanSourceService(ProcessService):

    def __init__(self, root_page:str, target_dir:str) -> None:
        self._root_page = root_page
        self._target_dir = target_dir
        self._processed_pages = []

    def _do_page_processing(self, page:Page) -> None:
        self._write_html_page(page = page) #relative_path=site_path, html=page.get_html())

        files = page.get_files()
        for key in files.keys():
            self._copy_file(relative_path=key, source_path=files[key])


    # def process(self) -> None:
    #     """
    #         iterate down from the root_page to all its linked sub-pages
    #         copy each page file to the correct relative location in target
    #         copy each linked resource from the source path to the target path
    #         create all dirs at target path as needed
    #     """
    #     self._process_page(
    #         source_path=self._root_page,
    #         site_path='index.html'
    #     )

    # def _process_page(self, source_path:str, site_path:str) -> dict:
    #     """
    #         create a Page object

    #         copy page html to new location

    #         extract all linked files
    #         copy linked files

    #         extract all linked pages
    #         runs this method recursively on linked pages
    #     """
    #     if not os.path.exists(source_path):
    #         # print("Source path does not exist: {}".format(source_path))
    #         return

    #     if source_path in self._processed_pages:
    #         """
    #             don't process pages twice
    #         """
    #         return

    #     print("Processing page {}".format(source_path))

    #     try:

    #         with open(source_path, mode="r", encoding='utf-8') as f:
    #             html = f.read()

    #             page = Page(source_path=source_path, html=html, site_path=site_path)
    #             # copy page html to new location
    #             # from source_file to target/"relative_path_of_page"
    #             self._write_html_page(relative_path=site_path, html=page.get_html())

    #             files = page.get_files()
    #             for key in files.keys():
    #                 self._copy_file(relative_path=key, source_path=files[key])

    #             pages = page.get_pages()

    #             # page_site_dir = os.path.dirname(site_path)

    #             self._processed_pages.append(source_path)

    #             for key in pages.keys():

    #                 print("Extracted page {} from {}".format(pages[key], source_path))

    #                 # sub_site_path = os.path.join(page_site_dir, key)
    #                 self._process_page(source_path=pages[key], site_path=key)

    #     except Exception as e:
    #         print ("ERROR processing {} : {}".format(source_path, e))


    #def _write_html_page(self, relative_path:str, html:str) -> None:
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


    def _ensure_directory_exists(self, path:str) -> None:
        location = os.path.dirname(path)
        try:
            os.makedirs(name=location)
        except FileExistsError:
            pass

