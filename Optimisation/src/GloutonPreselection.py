import opti_boxes as opt_box, getData as data
from EvalSolution import EvalSolution as eval
from Algorithme import Algorithme

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

EVAL = eval()

class GloutonPreselection(Algorithme):

    def __init__(self):
        super().__init__()
    
    def run(self) -> str:
        return self.main()

    def findBestToy(self, index, listToy, listBox):
        max=-999
        userBox = listBox[index]
        bestToy = None
        for toy in listToy:
            if userBox.canAddToBox(toy):
                userBox.addToBox(toy)
                note = EVAL.evaluate(listBox)
                userBox.delFromBox(toy)
                if note>max:
                    max=note
                    bestToy = toy
        return bestToy


    def buildBoxes(self, listUser, listToy, listBox):
        listAdd=[]
        for i in range(len(listUser)):
            toy=self.findBestToy(i,listToy,listBox)
            while toy is not None and toy in listAdd:
                listTemp = listToy.copy()
                if toy in listTemp:
                    listTemp.remove(toy)
                else:
                    break
                toy = self.findBestToy(i, listTemp, listBox)
            listAdd.append(toy)
        for i in range(len(listAdd)):
            toy = listAdd[i]
            if toy is not None and toy in listToy:
                listBox[i].addToBox(toy)
                listToy.remove(toy)

    def main(self) -> str:
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
            if(len(listBB)!=0): self.buildBoxes(listBB, listToyBB, listBoxBB)
            if(len(listPE)!=0): self.buildBoxes(listPE, listToyPE, listBoxPE)
            if(len(listEN)!=0): self.buildBoxes(listEN, listToyEN, listBoxEN)
            if(len(listAD)!=0): self.buildBoxes(listAD, listToyAD, listBoxAD)

        
        listBox=listBoxBB+listBoxPE+listBoxEN+listBoxAD
        res : str = str(EVAL.evaluate(listBox)) + "\n"

        for box in listBox :
            for toy in box.toys :
                res += box.childBelonging.id+ ";"+ toy.id+ ";"+ toy.category+ ";"+ toy.age+ ";"+ toy.state+"\n"

        return res

if __name__ == "__main__" :
    print(GloutonPreselection().run())