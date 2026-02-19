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

    def __hash__(self):
        return hash(self.id)


class Box() :

    def __init__(self, child : Child, maximumMass : int):
        self.toys : list[Toy] = []
        self.totalMass = 0
        self.totalPrice = 0
        self.childBelonging = child
        self.maximumMass = maximumMass

    def canAddToBox(self, toy : Toy) -> bool:
        return toy.mass+self.totalMass <= self.maximumMass and self.childBelonging.belongsToAge(toy.age)

    def canAddToBoxCheck(self, toy: Toy):
        if not toy.mass+self.totalMass <= self.maximumMass:
            return "mass !"
        if not self.childBelonging.belongsToAge(toy.age):
            return "age !"

    def addToBox(self, toy : Toy) :
        self.toys.append(toy)
        self.totalMass += toy.mass
        self.totalPrice += toy.price

    def delFromBox(self, toy : Toy) :
        self.toys.remove(toy)
        self.totalMass -= toy.mass
        self.totalPrice -= toy.price

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
            print("yohoho !")
            return ([],[])
        newBoxes = copy_boxes(self.boxes)
        newToys = copy_toys(self.toys)
        newBoxes[box].addToBox(newToys[toy])
        newToys.remove(newToys[toy])
        return (newBoxes, newToys)

def copy_boxes(boxes : list[Box]) -> list[Box]:
    res: list[Box] = []
    for box in boxes:
        newBox = Box(box.childBelonging, box.maximumMass)
        newBox.totalMass = box.totalMass
        newBox.toys = copy_toys(box.toys)
        newBox.totalPrice = box.totalPrice
        res.append(newBox)

    return res

def copy_toys(toys : list[Toy]) -> list[Toy]:
    res : list[Toy] = []
    for toy in toys :
        res.append(Toy(toy.id, toy.mass, toy.price, toy.category, toy.age, toy.state))

    return res
