import opti_boxes as opt_box, getData as data
from EvalSolution import EvalSolution as eval

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

@staticmethod
def findBestToy(index, listToy, listBox):
    evaluator = eval()
    max=-999
    userBox = listBox[index]
    bestToy = None
    for toy in listToy:
        if userBox.canAddToBox(toy):
            userBox.addToBox(toy)
            note = evaluator.evaluate(listBox)
            userBox.delFromBox(toy)
            if note>max:
                max=note
                bestToy = toy
    return bestToy


@staticmethod
def buildBoxes(listUser, listToy, listBox):
    listAdd=[]
    for i in range(len(listUser)):
        toy=findBestToy(i,listToy,listBox)
        while toy is not None and toy in listAdd:
            listTemp = listToy.copy()
            if toy in listTemp:
                listTemp.remove(toy)
            else:
                break
            toy = findBestToy(i, listTemp, listBox)
        listAdd.append(toy)

    
    for i in range(len(listAdd)):
        toy = listAdd[i]
        if toy is not None and toy in listToy:
            listBox[i].addToBox(toy)
            listToy.remove(toy)

class Glouton:

    data.get_data()
    listAbonnes = data.getAbonnes()
    listArticles = data.getArticles()
    massMax = data.getMassMax()

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
        box = opt_box.Box(child, massMax)
        listBoxBB.append(box)
    for child in listPE:
        box = opt_box.Box(child, massMax)
        listBoxPE.append(box)
    for child in listEN:
        box = opt_box.Box(child, massMax)
        listBoxEN.append(box)
    for child in listAD:
        box = opt_box.Box(child, massMax)
        listBoxAD.append(box)

    pairs = [
    (listToyBB, listBB),
    (listToyPE, listPE),
    (listToyEN, listEN),
    (listToyAD, listAD),
    ]

    listValMax = []

    for toy, child in pairs:
        if len(toy) != 0 and len(child) !=0:
            listValMax.append(len(toy) // len(child))
    maxbox = int(1 + min(listValMax)) if listValMax else 0

    for i in range(maxbox):
        if(len(listBB)!=0): buildBoxes(listBB, listToyBB, listBoxBB)
        if(len(listPE)!=0): buildBoxes(listPE, listToyPE, listBoxPE)
        if(len(listEN)!=0): buildBoxes(listEN, listToyEN, listBoxEN)
        if(len(listAD)!=0): buildBoxes(listAD, listToyAD, listBoxAD)

    
    listBox=listBoxBB+listBoxPE+listBoxEN+listBoxAD
    print("solution : ")
    for box in listBox :
        print("box de : ", box.childBelonging.id, ", ", box.childBelonging.age)
        for toy in box.toys :
            print("\t-", toy.id, toy.age, ", ", toy.category, ",", toy.mass, ", ", toy.state)
    
    evaluator = eval()
    print(evaluator.evaluate(listBox))
