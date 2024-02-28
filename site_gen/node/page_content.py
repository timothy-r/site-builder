from dataclasses import dataclass
from site_gen.node.linked_file import LinkedFile

@dataclass(frozen=True)
class PageContent():
    title:str

    source:LinkedFile

    download_file:LinkedFile

    sub_title:str = None

