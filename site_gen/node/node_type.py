from enum import Enum

class NodeType(Enum):

    """
        A directory album contains other directories
    """
    DIRECTORY = 1

    """
        A page album contains pages
    """
    PAGE = 2
