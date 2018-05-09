from classes.solution import Solution
from classes.evaluator import Evaluator

def main():
    # Solution handling
    solution = Solution(5, 5)
    solution.start()
    solution.print()

    # Evaluation
    evaluator = Evaluator()
    print(evaluator.shiftedSphere(solution.content, 0.3))
    print(evaluator.shiftedRosenbrock(solution.content, 0.3))
    print(evaluator.shiftedRastrign(solution.content, 0.3))
    
main()