from abc import ABC, abstractmethod


class Algorithme(ABC):

    @abstractmethod
    def run(self) -> str:
        pass