
from Algorithme import Algorithme
from Result import Result
import getData
from src.RecuitSimule import switchArticle

d = getData
d.get_data()
abonnes = d.getAbonnes()
articles = d.getArticles()
massMax = d.getMassMax()
print(switchArticle())

if __name__ == "__main__":
    algo : Algorithme = Algorithme() # Mettre l'algo voulu
    result = Result(algo)
    result.generateCsvString()
    result.saveToFile()
