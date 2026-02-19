from abc import ABC, abstractmethod

from EvalSolution import EvalSolution


class Algorithme(ABC):

    def __init__(self,  articles : list, abonnes : list, massMax : list):
        self.articles = articles
        self.abonnes = abonnes
        self.massMax = massMax
        self.eval = EvalSolution()

    @abstractmethod
    def run(self) -> str:
        pass