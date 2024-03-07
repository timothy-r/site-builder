from dataclasses import dataclass
from site_gen.node.linked_file import LinkedFile
from site_gen.node.album_type import NodeType

@dataclass(frozen=True)
class Album():

    """
        properties
            page - LinkedFile
            title - string
            sub_title - string (default is title)
            thumbnail:
                LinkedFile
                width
                height
                alt text
    """
    index_page:LinkedFile
    title:str
    type:NodeType
    thumbnail:LinkedFile
    thumbnail_width:int
    thumbnail_height:int
    thumbnail_alt:str = None
    sub_title:str = None



    # def rename_file_paths(self) -> None:
    #     self.index_page.rename_paths()
    #     self.thumbnail.rename_paths()

    # @property
    # def base_name(self) -> str:
    #     return self.index_page.base_name