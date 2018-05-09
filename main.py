from classes.solution import Solution
from classes.evaluator import Evaluator
from classes.hillClimb import HillClimb

def main():
    # Solution handling
    solution = Solution(100, 100)
    solution.start()
    solution.print()

    # Evaluation
    evaluator = Evaluator()
    print(evaluator.shiftedSphere(solution.content, 0.3))
    print(evaluator.shiftedRosenbrock(solution.content, 0.3))
    print(evaluator.shiftedRastrign(solution.content, 0.3))

    # HillClimb
    optimizer = HillClimb(solution, evaluator, 0, 100)
    print(optimizer.run())

main()