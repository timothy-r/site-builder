from abc import ABC, abstractmethod

class Reader(ABC):

    @abstractmethod
    def get_title() -> str:
        pass

    @abstractmethod
    def get_sub_title() -> str:
        pass

    @abstractmethod
    def get_contents(): # what type?
        pass

    @abstractmethod
    def get_children() -> list:
        pass
