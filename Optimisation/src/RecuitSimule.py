import random
from pickle import GLOBAL

import numpy as np

import opti_boxes, EvalSolution as eval, getData as data
from EvalSolution import EvalSolution

from opti_boxes import ProblemState

# Algo :
state = None
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
        box = opti_boxes.Box(child,massMax)
        listBoxes.append(box)

    global state
    state = ProblemState(listBoxes,listArticles)



def recuit() :
    initialisationProbleme()
    global state

    T = 50
    gamma = 0.995

    compteur = 0
    e = EvalSolution()
    while T > 1 :
        print(T)
        new_state = neighbour(state,T,20)
        e = EvalSolution()
        score1 = e.evaluate(state.boxes)
        score2 = e.evaluate(new_state.boxes)
        prob = accept_probability(score1,score2,T)
        T = T*gamma
        r= random.random()
        if prob>r :
            state = new_state
    string = "solution : \n"

    for box in state.boxes :
        string += "box de : " + box.childBelonging.id +  ", " +  box.childBelonging.age +"\n"
        for toy in box.toys :
            string+="\t-" +  toy.id +  toy.age + ", " +  toy.category+ "," +  str(toy.mass)+ ", " + toy.state + "\n"

    string += "score :" +  str(e.evaluate(state.boxes))+ "\n"
    return string



def neighbour(state, T, maxT):
    weights=[33,33,33]
    listOperator = []
    newState = ProblemState(opti_boxes.copy_boxes(state.boxes),opti_boxes.copy_toys(state.toys))

    dim = len(listBoxes)

    factor = 5

    nbr_operations = random.randint(1, 3)
    for _ in range(nbr_operations) :
        operator_choice = random.choices([0,1,2], weights=weights)[0]
        if operator_choice == 0:
            newState = switchArticle(newState)
        elif operator_choice == 1:
            newState = addArticle(newState)
        else:
            newState = delArticle(newState)
        listOperator.append(newState)

    return newState

def accept_probability(old_score, new_score, temperature):
    if new_score > old_score:
        return 1.0
    else:
        # The smaller the temperature, the smaller the probability of acceptance
        return np.exp((new_score - old_score) / temperature) # between 0 and 1

def switchArticle(state):
    non_empty_boxes = [box for box in state.boxes if len(box.toys) > 0]

    if len(non_empty_boxes) < 2:
        return state

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


    return state


def addArticle(state):
    if len(state.toys) == 0 or len(state.boxes) == 0:
        return state

    toy = random.choice(state.toys)
    box = random.choice(state.boxes)

    if box.canAddToBox(toy):
        box.addToBox(toy)
        state.toys.remove(toy)

    return state

def delArticle(state):

    non_empty_boxes = [box for box in state.boxes if len(box.toys) > 0]

    if not non_empty_boxes:
        return state

    box = random.choice(non_empty_boxes)
    toy = random.choice(box.toys)

    box.delFromBox(toy)
    state.toys.append(toy)

    return state



