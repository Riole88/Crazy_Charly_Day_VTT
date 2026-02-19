from src.opti_boxes import Toy, Child

FICHIER_DONNEES = "../donnees/02_pb_simples/pb1.csv"
def get_data ():
    with open(FICHIER_DONNEES, 'r') as f:
        lignes = f.readlines()  # Retourne une liste

    articles = []
    abonnes = []
    massMax = 0
    selector = -1
    for ligne in lignes:
        l = ligne.split(";")
        if "articles" in ligne:
            selector = 0
        elif "abonnes" in ligne :
            selector = 1
        elif "parametres" in ligne :
            selector = 2
        else :
            match selector :
                case 0 :
                    article = Toy(l[6],l[5],l[2],l[3])
                    articles.append(article)
                case 1 :
                    preferences =[l[3],l[4],l[5],l[6],l[7],l[8]]
                    abonne = Child(l[2],preferences)
                    abonnes.append(abonne)
                case 2 :
                    massMax = ligne