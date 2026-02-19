from Algorithme import Algorithme
from Result import Result
from src.RecuitAlgo import RecuitAlgo

if __name__ == "__main__":
    algo : Algorithme = RecuitAlgo() # Mettre l'algo voulu
    result = Result(algo)
    result.generateCsvString()
    result.saveToFile()
