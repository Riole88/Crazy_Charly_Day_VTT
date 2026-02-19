from Algorithme import Algorithme
from Glouton import AlgoGlouton
from GloutonPreselection import GloutonPreselection
from RecuitSimule import RecuitSimule
from Result import Result
from csvData import CsvData

if __name__ == "__main__":
    csvData = CsvData()
    csvData.readData("../donnees/02_pb_simples/pb3.csv")
    algo : Algorithme = GloutonPreselection(csvData.articles, csvData.abonnes, csvData.massMax) # Mettre l'algo voulu
    result = Result(algo)
    result.generateCsvString()
    result.saveToFile()
