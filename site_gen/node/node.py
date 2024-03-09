
"""
    a node in a tree of pages in a site
"""
class Node:

    def __init__(self, source_file:str) -> None:
        self._source_file = source_file

    @property
    def source_file(self) -> str:
        return self._source_file

    @property
    def title(self) -> str:
        pass