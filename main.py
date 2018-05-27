from classes.solution import Solution
from classes.evaluator import Evaluator
from classes.hillClimb import HillClimb

def main():
    # Solution handling
    solution = Solution(30, 5)
    solution.start()
    solution.print()
    
    # Evaluation
    evaluator = Evaluator()

    # HillClimb
    optimizer = HillClimb(100)
    
    # print(evaluator.shiftedSphere)

    optimizer.hillClimb(solution, evaluator.shiftedSphere, 1, 0.5)
    # print(optimizer.run())



main()