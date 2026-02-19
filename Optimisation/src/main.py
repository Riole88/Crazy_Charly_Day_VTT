from Algorithme import Algorithme
from Result import Result

if __name__ == "__main__":
    algo : Algorithme = Algorithme() # Mettre l'algo voulu
    result = Result(algo)
    result.generateCsvString()
    result.saveToFile()
