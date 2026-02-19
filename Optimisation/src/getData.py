from src.opti_boxes import Toy, Child

FICHIER_DONNEES = "../donnees/02_PB_simples/pb1.csv"
articles = []
abonnes = []
massMax = 0
def get_data ():
    with open(FICHIER_DONNEES, 'r') as f:
        lignes = f.readlines()  # Retourne une liste
    selector = -1

    for ligne in lignes :

        l = ligne.split(";")
        if "articles" in ligne:
            selector = 0
        elif "abonnes" in ligne :
            selector = 1
        elif "parametres" in ligne :
            selector = 2
        else :
            if ligne != "\n" :
                match selector :
                    case 0 :
                        article = Toy(l[0],int(l[6]),int(l[5]),l[2],l[3], l[4])
                        articles.append(article)
                    case 1 :
                        preferences =l[3].split(",")
                        abonne = Child(l[0],l[2],preferences)
                        abonnes.append(abonne)
                    case 2 :
                        global massMax
                        massMax = int(ligne)


def getAbonnes() :
        return abonnes
def getArticles() :
        return articles
def getMassMax() :
    return massMax
