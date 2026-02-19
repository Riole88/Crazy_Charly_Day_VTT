import os
from pathlib import Path

from Algorithme import Algorithme


class Result:

    def __init__(self, algorithme : Algorithme):
        self.algo : Algorithme = algorithme
        self.csv : str = ""

    def generateCsvString(self) -> None:
        self.csv = self.algo.run()

    def saveToFile(self) -> None:
        directory : str = "../out"
        if not Path(directory).exists():
            os.mkdir(directory)
        with open(f"{directory}/result.csv", "w") as f:
            f.write(self.csv)

    def __str__(self) -> str:
        return self.csv