from classes.solution import Solution
from classes.evaluator import Evaluator
from classes.hillClimb import HillClimb

def main():

    # Solution handling
    solution = Solution(100, 100)
    solution.start()
    # solution.print()
    
    # Evaluation
    evaluator = Evaluator()

    # HillClimb
    optimizer = HillClimb(100000)
    
    # # print(evaluator.shiftedSphere)

    optimizer.hillClimb(solution, evaluator.shiftedSphere, 1, 5)
    # print(optimizer.run())



main()