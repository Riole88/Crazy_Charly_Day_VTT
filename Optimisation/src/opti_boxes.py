class Child() :

    def __init__(self, id:str, age : str, preferences : list[str]):
        self.id = id
        self.age = age
        self.preferences = preferences

    def belongsToAge(self, ageToCheck:str) -> bool:
        return ageToCheck == self.age
    
class Toy():

    def __init__(self, id : str, mass: int, price : int, category : str, age : str, state:str):
        self.id = id
        self.mass = mass
        self.price = price
        self.category = category
        self.age = age
        self.state = state

    

class Box() :

    def __init__(self, child : Child, maximumMass : int):
        self.toys = []
        self.totalMass = 0
        self.totalPrice = 0
        self.childBelonging = child
        self.maximumMass = maximumMass

    def canAddToBox(self, toy : Toy) -> bool:
        return toy.mass+self.totalMass <= self.totalMass and self.childBelonging.belongsToAge(toy.age)


    def addToBox(self, toy : Toy) :
        self.toys.append(toy)
        self.totalMass += toy.mass
        self.totalPrice += toy.price

class ProblemState():

    def __init__(self, boxes : list[Box], toys : list[Toy]):
        self.boxes = boxes
        self.toys = toys

    def getPossibleActions(self) -> list[tuple[int, int]] :
        res : list[tuple[int, int]] = []

        for box in range(0,len(self.boxes)):
            for toy in range(0,len(self.toys)) :
                if self.boxes[box].canAddToBox(self.toys[toy]):
                    res.append((box, toy))

        return res
    

    def doAction(self, box : int, toy : int) -> tuple[list[Box], list[Toy]]:
        if not self.boxes[box].canAddToBox(self.toys[toy]):
            return ([],[])
        newBoxes = self.boxes.copy()
        newToys = self.toys.copy()
        newBoxes[box].addToBox(newToys[toy])
        newBoxes.remove(newBoxes[box])
        newToys.remove(newToys[toy])
        return (newBoxes, newToys)


