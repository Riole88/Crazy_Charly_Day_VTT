from opti_boxes import Box, Toy, ProblemState, Child
import getData
from EvalSolution import EvalSolution

EVAL = EvalSolution()

def resolve_problem(problem : ProblemState) -> ProblemState :
    possibleActions = problem.getPossibleActions()
    scoreMax : int = EvalSolution().evaluate(problem.boxes)
    bestState : ProblemState = problem

    #print("boxes length : ", len(bestState.boxes))

    for action in possibleActions :
        newLists = problem.doAction(action[0], action[1])
        newState = ProblemState(newLists[0], newLists[1])
        score : int = EvalSolution().evaluate(newState.boxes)
        #print("boxes : ", newState.boxes)
        #print("boxes length : ", len(newState.boxes))
        if score >= scoreMax:
            print("score : ", score)
            scoreMax = score
            bestState = newState

    return bestState


def main():

    d = getData
    d.get_data()
    abonnes = d.getAbonnes()
    articles = d.getArticles()
    massMax = d.getMassMax()
    print(massMax)

    listBoxes : list[Box] = []

    for abonne in abonnes :
        listBoxes.append(Box(abonne, massMax))

    problemToSolve : ProblemState = ProblemState(listBoxes, articles)

    solution : ProblemState = resolve_problem(problemToSolve)

    eval : EvalSolution = EvalSolution()

    oldScore : int = -999999
    newScore : int =eval.evaluate(solution.boxes)

    while oldScore != newScore :
        oldScore = newScore
        eval.reset_score()
        solution = resolve_problem(solution)
        newScore = eval.evaluate(solution.boxes)

    print("score max : ",newScore)
    print("solution : ")
    for box in solution.boxes :
        print("box de : ", box.childBelonging.id, ", ", box.childBelonging.age)
        for toy in box.toys :
            print("\t-", toy.id, toy.age, ", ", toy.category, ",", toy.mass, ", ", toy.state)


if __name__ == "__main__":
    main()


