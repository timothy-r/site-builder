import re

from bs4 import BeautifulSoup as bs

from site_gen.node.linked_file import LinkedFile

"""
    Handles extracting linked resources from a HTML document
"""
class Page:

    def __init__(self, source_path:str, html:str, site_path:str) -> None:
        self._source_path = source_path
        self._html = html
        self._site_path = site_path

        self._all_links:dict[LinkedFile] = {}

        # extract contents
        self._extract_contents()

    def get_pages(self) -> dict:
        """
            return a dict of link path : source_system_path
        """
        results = {}

        for file in self._all_links.values():
            if file.is_html_file and file.exists:
                results[file.site_file_path] = file.linked_file_path

        return results

    def get_files(self) -> dict:
        """
            return a dict of file path : source_system_path
        """
        results = {}

        for file in self._all_links.values():
            if file.is_media_file and file.exists:
                results[file.site_file_path] = file.linked_file_path
        return results

    def get_html(self) -> str:
        """
            respond with the html with href rewritten
            keep the original html doc intact
        """
        dom_doc = bs(self._html, 'html.parser')

        all_a_tags = dom_doc.find_all("a")
        for tag in all_a_tags:
            href = tag.get('href')
            base = href.split('@')[0]
            # configure this
            base = re.sub('main.php', 'index.html', base)
            tag['href'] = base

        return dom_doc.prettify()

    def _extract_contents(self) -> None:
        dom_doc = bs(self._html, 'html.parser')

        self._gather_all_tags(dom_doc=dom_doc, tag_name='a', attr='href')
        self._gather_all_tags(dom_doc=dom_doc, tag_name='link', attr='href')
        self._gather_all_tags(dom_doc=dom_doc, tag_name='img', attr='src')
        self._gather_all_tags(dom_doc=dom_doc, tag_name='iframe', attr='src')
        self._gather_all_tags(dom_doc=dom_doc, tag_name='object', attr='data')
        self._gather_all_tags(dom_doc=dom_doc, tag_name='embed', attr='src')

    def _gather_all_tags(self, dom_doc, tag_name:str, attr:str) -> None:
        for tag in dom_doc.find_all(tag_name):
            item = tag.get(attr)
            if item:
                base = item.split('@')[0]

                self._all_links[base] = LinkedFile(
                    link_path=base,
                    source_path=self._source_path,
                    site_path=self._site_path)
