from dataclasses import dataclass
from site_gen.node.linked_file import LinkedFile

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
    thumbnail:LinkedFile
    thumbnail_width:int
    thumbnail_heigth:int
    thumbnail_alt:str = None
    sub_title:str = None


