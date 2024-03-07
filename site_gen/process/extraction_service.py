import os
import logging

# import re
# import yaml
import shutil

from site_gen.node.page import Page
from site_gen.node.album import Album
from site_gen.file.yaml_file import YAMLFile

from site_gen.process.process_service import ProcessService

"""
    Generates the data files for a static site
    Updates the source contents, cleans up names etc
"""
class ExtractionService(ProcessService):

    def _do_page_processing(self, page:Page) -> None:

        logging.info("{} _do_page_processing {}".format(__class__.__name__, page))

        """
        switch behaviour on type of page
        index page
            process each sub folder
            create the file system folder
            generate the index.yml file with index data
            move the thumbnail images

        leaf page
            extract contents
            update index.yml
            move source files
        """
        page_file = page.get_file()

        # write to the index.yml file in the index directory of these albums
        index_file = os.path.join(
            self._target_dir,
            page_file.host_page_path_normalised,
            "index.yml")

        if page.is_index_file:

            logging.info("{}: Processing index page {}".format(__class__.__name__, page))

            for album in page.get_albums():
                logging.info("{}: Processing album: {}".format(__class__.__name__, album.index_page.file_system_path))

                album_path = os.path.join(
                    self._target_dir,
                    os.path.dirname(album.index_page.host_page_path_normalised))

                # self._ensure_sub_folders_exist(album_path)

                logging.info("{}: Processing album: page_file = {}".format(__class__.__name__, page_file))

                thumbnail_data_path = os.path.join(
                    page_file.host_page_path_normalised,
                    'thumbs',
                    album.thumbnail.file_name_normalised
                )

                self._update_index_data_file(
                    file_name=index_file,
                    album=album,
                    thumbnail_path=thumbnail_data_path
                )

                # copy thumbnail files to the target location
                thumbnail_target_path = os.path.join(
                    self._target_dir,
                    thumbnail_data_path
                )

                self._copy_thumbnail(album=album, target_path=thumbnail_target_path)
        else:
            pass
            # extract contents
            content = page.get_content()

            # # update index file

            # copy image / other content files

            logging.info("Processing content page {}".format(page))

    def _ensure_sub_folders_exist(self, path:str) -> None:
        """
            ensure for an index page there are these sub-folders
            # 'folders'
            # 'pages'
            'images'
            'thumbs'

        """
        # logging.info("ensure folder : {}".format(path))

        self._ensure_directory_exists(path=path)

        for dir in ['images', 'thumbs']:
            sub_path = os.path.join(path, dir)
            # logging.info("ensure sub folder : {}".format(sub_path))
            self._ensure_directory_exists(path=sub_path)

    def _update_index_data_file(self, file_name:str, album:Album, thumbnail_path:str) -> None:

        self._ensure_directory_exists(path=file_name)

        logging.info("{} _update_index_data_file {}".format(__class__.__name__, file_name))
        # try to read contents
        # update data
        # write data back to file

        key = album.index_page.base_name_normalised

        yaml_file = YAMLFile(path=file_name)
        data = yaml_file.read()

        if not 'contents' in data:
            data['contents'] = {}

        if not key in data['contents']:
            data['contents'][key] = {}

        data['contents'][key]['title'] = album.title
        data['contents'][key]['sub_title'] = album.sub_title
        data['contents'][key]['type'] = album.type.name
        data['contents'][key]['thumb'] = {}
        data['contents'][key]['thumb']['src'] = thumbnail_path
        data['contents'][key]['thumb']['height'] = album.thumbnail_height
        data['contents'][key]['thumb']['width'] = album.thumbnail_width
        data['contents'][key]['thumb']['alt'] = album.thumbnail_alt

        yaml_file.write(data=data)

    def _copy_thumbnail(self, album:Album, target_path:str) -> None:
        logging.info("copy thumbnail file {}".format(target_path))

        self._ensure_directory_exists(path=target_path)

        if not os.path.exists(target_path):
            # logging.info("Copy file from {} to {}".format(source_path, target_path))
            shutil.copy(album.thumbnail.file_system_path, target_path)
