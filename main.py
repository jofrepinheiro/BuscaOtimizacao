from classes.solution import Solution
from classes.evaluator import Evaluator
from classes.hillClimb import HillClimb

def main():
    # Solution handling
    solution = Solution(30, 5)
    solution.start()
    solution.print()

    # # TWEAK TEST
    for i in range(0,10):
        solution.tweak(1, 2)
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