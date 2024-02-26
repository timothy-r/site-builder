import os
# import re
import yaml
import shutil

from site_gen.node.page import Page
from site_gen.node.album import Album

from site_gen.process.process_service import ProcessService

"""
    Generates the data files for a static site
    Updates the source contents, cleans up names etc
"""
class ExtractionService(ProcessService):

    def __init__(self, root_page:str, target_dir:str) -> None:
        super().__init__(root_page=root_page, target_dir=target_dir)


    def _do_page_processing(self, page:Page) -> None:
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
        if page.is_index_file:
            print("Processing index page {}".format(page))

            # albums = page.get_albums()

            for album in page.get_albums():
                print("Processing album: {}".format(album.index_page.file_system_path))

                album_path = os.path.join(
                    self._target_dir,
                    os.path.dirname(album.index_page.site_file_path_normalised))

                self._ensure_sub_folders_exist(album_path)

                page_file = page.get_file()

                # write to the index.yml file in the index directory of these albums
                index_file = os.path.join(
                    self._target_dir,
                    os.path.dirname(page_file.site_file_path_normalised),
                    "index.yml") # page.site_path + '/index.yml'

                thumbnail_data_path = os.path.join(
                    os.path.dirname(page_file.site_file_path_normalised),
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
                    os.path.dirname(page_file.site_file_path_normalised),
                    'thumbs',
                    album.thumbnail.file_name_normalised
                )

                self._copy_thumbnail(album=album, target_path=thumbnail_target_path)
        else:
            pass
            # print("Processing content page {}".format(page))

    def _ensure_sub_folders_exist(self, path:str) -> None:
        """
            ensure for an index page there are these sub-folders
            # 'folders'
            # 'pages'
            'images'
            'thumbs'

        """
        print("ensure folder : {}".format(path))

        self._ensure_directory_exists(path=path)

        for dir in ['images', 'thumbs']:
            sub_path = os.path.join(path, dir)
            print("ensure sub folder : {}".format(sub_path))
            self._ensure_directory_exists(path=sub_path)

    def _update_index_data_file(self, file_name:str, album:Album, thumbnail_path:str) -> None:
        # try to read contents
        # update data
        # write data back to file

        key = album.index_page.base_name_normalised

        data = self._read_yaml(path=file_name)

        if not 'contents' in data:
            data['contents'] = {}

        if not key in data['contents']:
            data['contents'][key] = {}

        data['contents'][key]['title'] = album.title
        data['contents'][key]['sub_title'] = album.sub_title
        data['contents'][key]['type'] = 'dir'
        data['contents'][key]['thumb'] = {}
        data['contents'][key]['thumb']['src'] = thumbnail_path
        data['contents'][key]['thumb']['height'] = album.thumbnail_height
        data['contents'][key]['thumb']['width'] = album.thumbnail_width
        data['contents'][key]['thumb']['alt'] = album.thumbnail_alt

        self._write_yaml(path=file_name, data=data)

    def _copy_thumbnail(self, album:Album, target_path:str) -> None:
        print("copy thumbnail file {}".format(target_path))

        self._ensure_directory_exists(path=target_path)

        if not os.path.exists(target_path):
            # print("Copy file from {} to {}".format(source_path, target_path))
            shutil.copy(album.thumbnail.file_system_path, target_path)

    def _read_yaml(self, path:str) -> dict:
        """
            read yaml file at path
        """
        if os.path.exists(path=path):
            with open(path, 'r') as file:
                data = yaml.safe_load(file)
                return data
        else:
            return {}

    def _write_yaml(self, path:str, data:dict) -> None:
        with open(path, 'w') as file:
            file.write(yaml.safe_dump(data=data))