import argparse

from Algorithme import Algorithme
from Glouton import AlgoGlouton
from GloutonPreselection import GloutonPreselection
from RecuitSimule import RecuitSimule
from Result import Result
from csvData import CsvData

def runAlgo(algo: Algorithme) -> None:
    result = Result(algo)
    result.generateCsvString()
    result.saveToFile()

def runAllAlgo() -> None:
    resultGloutonPreselection : str = GloutonPreselection(csvData.articles, csvData.abonnes, csvData.massMax).run()
    resultGlouton : str = AlgoGlouton(csvData.articles, csvData.abonnes, csvData.massMax).run()
    resultRecuite : str = RecuitSimule(csvData.articles, csvData.abonnes, csvData.massMax).run()

    results = {
        "GloutonPreselection": resultGloutonPreselection,
        "Glouton": resultGlouton,
        "RecuitSimule": resultRecuite
    }

    meilleur_algo = max(results, key=results.get)
    meilleur_solution = results[meilleur_algo]

    print(f"Meilleur algorithme: {meilleur_algo}")
    print(f"Meilleur score: {meilleur_solution}")

if __name__ == "__main__":
    parser : argparse.ArgumentParser = argparse.ArgumentParser(description="Choix de l'algorithme à utiliser")
    parser.add_argument('Algorithme', choices=['GloutonPreselection', 'Glouton', 'RecuitSimule', 'Best'])
    args = parser.parse_args()

    csvData = CsvData()
    csvData.readData("../donnees/02_pb_simples/pb3.csv")

    algo: Algorithme

    match args.Algorithme:
        case "GloutonPreselection":
            algo = GloutonPreselection(csvData.articles, csvData.abonnes, csvData.massMax)
            runAlgo(algo)
        case "Glouton":
            algo = AlgoGlouton(csvData.articles, csvData.abonnes, csvData.massMax)
            runAlgo(algo)
        case "RecuitSimule":
            algo = RecuitSimule(csvData.articles, csvData.abonnes, csvData.massMax)
            runAlgo(algo)
        case "Best":
            runAllAlgo()