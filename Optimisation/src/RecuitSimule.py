import random

import opti_boxes, EvalSolution as eval, getData as data
from src.main import articles

# Algo :
listBB = []
listPE = []
listEN = []
listAD = []
listToyBB = []
listToyPE = []
listToyEN = []
listToyAD = []
listBoxBB = []
listBoxPE = []
listBoxEN = []
listBoxAD = []
listBoxes = []

def initialisationProbleme() :
    data.get_data()
    listAbonnes = data.getAbonnes()
    listArticles = data.getArticles()
    massMax = data.getMassMax()

    #Récupérer les listes de tous les utilisateurs
    for child in listAbonnes:
        match child.age:
            case "BB": listBB.append(child)
            case "PE": listPE.append(child)
            case "EN": listEN.append(child)
            case "AD": listAD.append(child)

    for toy in listArticles:
        match toy.age:
            case "BB": listToyBB.append(toy)
            case "PE": listToyPE.append(toy)
            case "EN": listToyEN.append(toy)
            case "AD": listToyAD.append(toy)

    for child in listBB:
        box = opti_boxes.Box(child, massMax)
        listBoxBB.append(box)
    for child in listPE:
        box = opti_boxes.Box(child, massMax)
        listBoxPE.append(box)
    for child in listEN:
        box = opti_boxes.Box(child, massMax)
        listBoxEN.append(box)
    for child in listAD:
        box = opti_boxes.Box(child, massMax)
        listBoxAD.append(box)
    listBoxes.append(listBoxAD)
    listBoxes.append(listBoxEN)
    listBoxes.append(listBoxPE)
    listBoxes.append(listBoxBB)


def recuit(solutionInitiale) :
    T = 10


def switchArticle() :
    initialisationProbleme()

    size = len(listBoxes)
    r = random.randint(0,size)
    r2 = random.randint(0,size)
    while r2 == r :
        r2 = random.randint(0,size)
    size1 = len(listBoxes[r].toys)
    size2 = len(listBoxes[r2].toys)
    r3 = random.randint(0,size1)
    r4 = random.randint(0,size2)
    toy1 = listBoxes[r].toys[r3]
    listBoxes[r].delFromBox(toy1)
    toy2 = listBoxes[r2].toys[r4]
    listBoxes[r2].delFromBox(toy2)

    if listBoxes[r].canAddToBox(toy2) :
        listBoxes[r].addToBox(toy2)
    else :
        articles.append(toy2)
    if listBoxes[r2].canAddToBox(toy1) :
        listBoxes[r2].addToBox(toy1)
    else :
        articles.append(toy1)

def addArticle() :
    toy = None
    if len(articles) != 0 :
        r = random.randint(0,len(articles))
        toy = articles[r]
    rAbonne = random.randint(0,len(listBoxes))
    if listBoxes[rAbonne].canAddToBox(toy) :
        listBoxes[rAbonne].addToBox(toy)
        articles.remove(toy)
def delArticle() :
    size = len(listBoxes)
    r = random.randint(0,size)
    size2 = len(listBoxes[r].toys)
    r2 = random.randint(0,size2)
    toy = listBoxes[r].toys[r2]
    listBoxes[r].delFromBox(toy)


