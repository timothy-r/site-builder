import re
import pathlib

from bs4 import BeautifulSoup as bs

from site_gen.node.linked_file import LinkedFile
from site_gen.node.album import Album

"""
    Handles extracting linked resources from a HTML document
"""
class Page:

    def __init__(self, source_path:str, html:str, site_path:str) -> None:
        """
            source_path: the file system path of this page
            html: the HTML source of this page
            site_path: the path to this file on the site it belongs to
        """
        self._source_path = source_path
        self._html = html
        self._site_path = site_path

        self._all_links:dict[LinkedFile] = {}

        # extract contents
        self._extract_contents()

    def __repr__(self) -> str:
        return "Page(source_path='{}', site_path='{}')".format(self._source_path, self._site_path)

    @property
    def site_path(self) -> str:
        return self._site_path

    def get_file(self) -> LinkedFile:
        return LinkedFile(link_path=self._site_path, source_path=self._source_path, parent_path='')

    def get_pages(self) -> dict:
        """
            return a dict of link path : source_system_path
        """
        results = {}

        for file in self._all_links.values():
            if file.is_html_file and file.exists:
                results[file.site_file_path] = file.file_system_path

        return results

    def get_files(self) -> dict:
        """
            return a dict of file path : source_system_path
        """
        results = {}

        for file in self._all_links.values():
            if file.is_media_file and file.exists:
                results[file.site_file_path] = file.file_system_path
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

    def get_albums(self) -> list[Album]:
        """
            extract the albums from an index page
        """
        if not self.is_index_file:
            return []

        dom_doc = bs(self._html, 'html.parser')

        albums = []
        # album exist in a div with class 'gallery-album'
        for album in dom_doc.find_all(name="div", attrs={'class': 'gallery-album'}):

            albums.append(self._read_album(album=album))

        return albums

    def _read_album(self, album) -> Album:
        """
            extract Album data from a HTML dom element
        """
        # links = album.find_all('a')

        # for link in links:
            # album_path = link.get('href')

        h4 = album.find('h4')
        title = h4.find('a').text.strip()
        album_path = h4.find('a').get('href')

        sub_title = album.find('p').text.strip()
        thumb_nail = album.find('img')

        return Album(
            index_page = LinkedFile(
                link_path=album_path,
                source_path=self._source_path,
                parent_path=self._site_path),
            title = title,
            sub_title = sub_title,
            thumbnail = LinkedFile(
                link_path=thumb_nail.get('src'),
                source_path=self._source_path,
                parent_path=self._site_path),
            thumbnail_alt = thumb_nail.get('alt'),
            thumbnail_height = int(thumb_nail.get('height')),
            thumbnail_width = int(thumb_nail.get('width'))
        )

    @property
    def is_index_file(self) -> bool:
        """
            is this an index page?
        """
        return pathlib.PurePath(self._site_path).name == 'index.html'


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
                    parent_path=self._site_path)
