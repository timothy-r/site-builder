from abc import ABC, abstractmethod

class ProcessService(ABC):

    @abstractmethod
    def process(self) -> None:
        pass