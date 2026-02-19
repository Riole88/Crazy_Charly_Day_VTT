import opti_boxes as opt_box
from Algorithme import Algorithme
from csvData import CsvData

class GloutonPreselection(Algorithme):

    def __init__(self,  articles : list, abonnes : list, massMax : list):
        super().__init__(articles, abonnes, massMax)
        self.listBB = []
        self.listPE = []
        self.listEN = []
        self.listAD = []
        self.listToyBB = []
        self.listToyPE = []
        self.listToyEN = []
        self.listToyAD = []
        self.listBoxBB = []
        self.listBoxPE = []
        self.listBoxEN = []
        self.listBoxAD = []
    
    def run(self) -> str:
        return self.main()

    def findBestToy(self, index, listToy, listBox):
        max=-999
        userBox = listBox[index]
        bestToy = None
        for toy in listToy:
            if userBox.canAddToBox(toy):
                userBox.addToBox(toy)
                note = self.eval.evaluate(listBox)
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
        for child in self.abonnes:
            match child.age:
                case "BB": self.listBB.append(child)
                case "PE": self.listPE.append(child)
                case "EN": self.listEN.append(child)
                case "AD": self.listAD.append(child)

        for toy in self.articles:
            match toy.age:
                case "BB": self.listToyBB.append(toy)
                case "PE": self.listToyPE.append(toy)
                case "EN": self.listToyEN.append(toy)
                case "AD": self.listToyAD.append(toy)

        for child in self.listBB:
            box = opt_box.Box(child, self.massMax)
            self.listBoxBB.append(box)
        for child in self.listPE:
            box = opt_box.Box(child, self.massMax)
            self.listBoxPE.append(box)
        for child in self.listEN:
            box = opt_box.Box(child, self.massMax)
            self.listBoxEN.append(box)
        for child in self.listAD:
            box = opt_box.Box(child, self.massMax)
            self.listBoxAD.append(box)

        pairs = [
        (self.listToyBB, self.listBB),
        (self.listToyPE, self.listPE),
        (self.listToyEN, self.listEN),
        (self.listToyAD, self.listAD),
        ]

        listValMax = []

        for toy, child in pairs:
            if len(toy) != 0 and len(child) !=0:
                listValMax.append(len(toy) // len(child))
        maxbox = int(1 + min(listValMax)) if listValMax else 0

        for i in range(maxbox):
            if len(self.listBB)!=0: self.buildBoxes(self.listBB, self.listToyBB, self.listBoxBB)
            if len(self.listPE)!=0: self.buildBoxes(self.listPE, self.listToyPE, self.listBoxPE)
            if len(self.listEN)!=0: self.buildBoxes(self.listEN, self.listToyEN, self.listBoxEN)
            if len(self.listAD)!=0: self.buildBoxes(self.listAD, self.listToyAD, self.listBoxAD)

        
        listBox=self.listBoxBB+self.listBoxPE+self.listBoxEN+self.listBoxAD
        self.bestScore = self.eval.evaluate(listBox)
        res : str = str(self.bestScore) + "\n"

        for box in listBox :
            res += f"{box.childBelonging.id};"

            for toy in box.toys :
                res += f"{toy.category};{toy.age};{toy.state}"
            res += "\n"

        print("Glouton avec préselection - score: ", self.bestScore)
        return res

if __name__ == "__main__" :
    csvData = CsvData()
    csvData.readData("../donnees/02_pb_simples/pb3.csv")
    print(GloutonPreselection(csvData.articles, csvData.abonnes, csvData.massMax).run())