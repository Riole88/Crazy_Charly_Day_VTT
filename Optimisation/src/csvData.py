import os

from opti_boxes import Toy, Child

class CsvData:

    def __init__(self):
        self.articles = []
        self.abonnes = []
        self.massMax = 0

    def readData(self, dataPath : str) -> None:
        self.articles = []
        self.abonnes = []
        self.massMax = 0

        script_dir = os.path.dirname(os.path.abspath(__file__))
        full_path = os.path.join(script_dir, dataPath)

        print(os.getcwd())
        with open(full_path, 'r') as f:
            lignes = f.readlines()  # Retourne une liste
        selector = -1

        for ligne in lignes:

            l = ligne.split(";")
            if "articles" in ligne:
                selector = 0
            elif "abonnes" in ligne:
                selector = 1
            elif "parametres" in ligne:
                selector = 2
            else:
                if ligne != "\n":
                    match selector:
                        case 0:
                            article = Toy(l[0], int(l[6]), int(l[5]), l[2], l[3], l[4])
                            self.articles.append(article)
                        case 1:
                            preferences = l[3].split(",")
                            abonne = Child(l[0], l[2], preferences)
                            self.abonnes.append(abonne)
                        case 2:
                            self.massMax = int(ligne)

    def getAbonnes(self):
        return self.abonnes

    def getArticles(self):
        return self.articles

    def getMassMax(self):
        return self.massMax

