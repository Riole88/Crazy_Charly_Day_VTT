from csvData import CsvData
from opti_boxes import Box, ProblemState
from src.Algorithme import Algorithme

class AlgoGlouton(Algorithme):

    def __init__(self,  articles : list, abonnes : list, massMax : list):
        super().__init__(articles, abonnes, massMax)

    def run(self) -> str:
        return self.main()

    def resolve_problem(self, problem : ProblemState) -> ProblemState :
        possibleActions = problem.getPossibleActions()
        scoreMax : int = self.eval.evaluate(problem.boxes)
        bestState : ProblemState = problem

        #print("boxes length : ", len(bestState.boxes))

        for action in possibleActions :
            newLists = problem.doAction(action[0], action[1])
            newState = ProblemState(newLists[0], newLists[1])
            score : int = self.eval.evaluate(newState.boxes)
            #print("boxes : ", newState.boxes)
            #print("boxes length : ", len(newState.boxes))
            if score >= scoreMax:
                # print("score : ", score)
                scoreMax = score
                bestState = newState

        return bestState


    def main(self) -> str:
        # print(self.massMax)

        listBoxes : list[Box] = []

        for abonne in self.abonnes :
            listBoxes.append(Box(abonne, self.massMax))

        problemToSolve : ProblemState = ProblemState(listBoxes, self.articles)

        solution : ProblemState = self.resolve_problem(problemToSolve)

        oldScore : int = -999999
        newScore : int = self.eval.evaluate(solution.boxes)

        while oldScore != newScore :
            oldScore = newScore
            solution = self.resolve_problem(solution)
            newScore = self.eval.evaluate(solution.boxes)

        res : str = str(newScore) + "\n"

        for box in solution.boxes :
            res += f"{box.childBelonging.id};"

            for toy in box.toys :
                res += f"{toy.category};{toy.age};{toy.state}"
            res += "\n"

        self.bestScore = newScore
        print("Glouton - score: ", self.bestScore)

        return res


if __name__ == "__main__" :
    csvData = CsvData()
    csvData.readData("../donnees/02_pb_simples/pb3.csv")
    print(AlgoGlouton(csvData.articles, csvData.abonnes, csvData.massMax).run())
