from abc import ABC, abstractmethod

class Reader(ABC):

    @abstractmethod
    def get_title(self) -> str:
        pass

    @abstractmethod
    def get_sub_title(self) -> str:
        pass

    @abstractmethod
    def get_contents(self): # what type?
        pass

    @abstractmethod
    def get_children(self) -> list:
        pass
