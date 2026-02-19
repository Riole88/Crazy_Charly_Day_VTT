from opti_boxes import Box, ProblemState
import getData
from EvalSolution import EvalSolution
from src.Algorithme import Algorithme

EVAL = EvalSolution()

class AlgoUCS(Algorithme):

    def __init__(self):
        super().__init__()

    def run(self) -> str:
        return self.main()

    def resolve_problem(self, problem : ProblemState) -> ProblemState :
        possible_actions = problem.getPossibleActions()
        score_max : int = EVAL.evaluate(problem.boxes)
        best_state : ProblemState = problem

        #print("boxes length : ", len(bestState.boxes))

        for action in possible_actions :
            newLists = problem.doAction(action[0], action[1])
            newState = ProblemState(newLists[0], newLists[1])
            score : int = EVAL.evaluate(newState.boxes)
            #print("boxes : ", newState.boxes)
            #print("boxes length : ", len(newState.boxes))
            if score >= score_max:
                print("score : ", score)
                score_max = score
                best_state = newState

        return best_state


    def main(self) -> str:

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

        solution : ProblemState = self.resolve_problem(problemToSolve)

        eval : EvalSolution = EvalSolution()

        oldScore : int = -999999
        newScore : int =eval.evaluate(solution.boxes)

        while oldScore != newScore :
            oldScore = newScore
            solution = self.resolve_problem(solution)
            newScore = eval.evaluate(solution.boxes)

        res : str = str(newScore) + "\n"

        for box in solution.boxes :
            for toy in box.toys :
                res += box.childBelonging.id+ ";"+ toy.id+ ";"+ toy.category+ ";"+ toy.age+ ";"+ toy.state+"\n"

        return res


if __name__ == "__main__" :
    print(AlgoUCS().run())