import random

import numpy as np

import opti_boxes
from Algorithme import Algorithme
from EvalSolution import EvalSolution
from opti_boxes import ProblemState

class RecuitSimule(Algorithme):

    def __init__(self,  articles : list, abonnes : list, massMax : list):
        super().__init__(articles, abonnes, massMax)
        self.state = ProblemState([], [])
        self.listBoxes = []

    def run(self) -> str:
        return self.recuit()

    def initialisationProbleme(self) :
        #Récupérer les listes de tous les utilisateurs
        for child in self.abonnes:
            box = opti_boxes.Box(child, self.massMax)
            self.listBoxes.append(box)

        self.state = ProblemState(self.listBoxes, self.articles)


    def recuit(self) :
        self.initialisationProbleme()

        T = 50
        gamma = 0.995

        e = EvalSolution()
        while T > 1 :
            print(T)
            new_state = self.neighbour()
            e = EvalSolution()
            score1 = e.evaluate(self.state.boxes)
            score2 = e.evaluate(new_state.boxes)
            prob = self.accept_probability(score1, score2, T)
            T = T*gamma
            r= random.random()
            if prob>r :
                self.state = new_state
        string = "solution : \n"

        for box in self.state.boxes :
            string += "box de : " + box.childBelonging.id +  ", " +  box.childBelonging.age +"\n"
            for toy in box.toys :
                string+="\t-" +  toy.id +  toy.age + ", " +  toy.category+ "," +  str(toy.mass)+ ", " + toy.state + "\n"

        string += "score :" +  str(e.evaluate(self.state.boxes))+ "\n"
        return string



    def neighbour(self) -> ProblemState:
        weights=[33,33,33]
        listOperator = []
        newState = ProblemState(opti_boxes.copy_boxes(self.state.boxes),opti_boxes.copy_toys(self.state.toys))

        nbr_operations = random.randint(1, 3)
        for _ in range(nbr_operations) :
            operator_choice = random.choices([0,1,2], weights=weights)[0]
            if operator_choice == 0:
                newState = self.switchArticle(newState)
            elif operator_choice == 1:
                newState = self.addArticle(newState)
            else:
                newState = self.delArticle(newState)
            listOperator.append(newState)

        return newState

    def accept_probability(self, old_score, new_score, temperature) -> float:
        if new_score > old_score:
            return 1.0
        else:
            return np.exp((new_score - old_score) / temperature) # Entre 0 et 1

    def switchArticle(self, newState):
        non_empty_boxes = [box for box in newState.boxes if len(box.toys) > 0]

        if len(non_empty_boxes) < 2:
            return newState

        box1 = random.choice(non_empty_boxes)
        box2 = random.choice(non_empty_boxes)

        while box2 == box1:
            box2 = random.choice(non_empty_boxes)

        toy1 = random.choice(box1.toys)
        toy2 = random.choice(box2.toys)

        if box1.canAddToBox(toy2) and box2.canAddToBox(toy1):
            box1.delFromBox(toy1)
            box2.delFromBox(toy2)

            box1.addToBox(toy2)
            box2.addToBox(toy1)


        return newState


    def addArticle(self, newState):
        if len(newState.toys) == 0 or len(newState.boxes) == 0:
            return newState

        toy = random.choice(newState.toys)
        box = random.choice(newState.boxes)

        if box.canAddToBox(toy):
            box.addToBox(toy)
            newState.toys.remove(toy)

        return newState

    def delArticle(self, newState):
        non_empty_boxes = [box for box in newState.boxes if len(box.toys) > 0]

        if not non_empty_boxes:
            return newState

        box = random.choice(non_empty_boxes)
        toy = random.choice(box.toys)

        box.delFromBox(toy)
        newState.toys.append(toy)

        return newState



