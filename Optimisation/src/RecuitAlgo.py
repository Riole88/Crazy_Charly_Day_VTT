from src.Algorithme import Algorithme
from src.RecuitSimule import recuit


class RecuitAlgo (Algorithme) :
    def run(self) -> str:
        return recuit()