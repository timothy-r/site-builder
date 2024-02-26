import os
import re

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
            albums = page.get_albums()
            for album in albums:
                print("Processing album: {}".format(album.index_page.file_system_path))
                # strip leading v/ from the path
                album_path = os.path.dirname(album.index_page.site_file_path)

                album_path = re.sub(
                    pattern='^v/',
                    repl='',
                    string=album_path
                )

                # album_path = album_path.replace('/v', '')
                album_path = os.path.join(self._target_dir, album_path)

                album_path = self._normalise_file_name(album_path)

                self._ensure_sub_folders_exist(album_path)

                # write to the index.yml file in the index directory
                album_index_file = album_path + '/index.yml'
                self._update_data_file(file_name=album_index_file, album=album)

                # copy thumbnail files to the target location
        else:
            pass
            # print("Processing content page {}".format(page))

    def _normalise_file_name(self, name:str) -> str:
        name = name.lower()
        name = name.replace('+','_')
        name = name.replace('-', '_')
        return name

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


    def _update_data_file(self, file_name:str, album:Album) -> None:
        # try to read contents
        # update data
        # write data back to file
        pass

    def _copy_thumbnail(self) -> None:
        pass