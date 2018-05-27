from classes.solution import Solution
from classes.evaluator import Evaluator
from classes.hillClimb import HillClimb
from classes.simAnealling import SimulatedAnnealing

def main():

    # Evaluator
    evaluator = Evaluator()



    # HillClimb
    # solution = Solution(100, 50)
    # solution.start()
    # optimizer = HillClimb(100000)
    # optimizer.run(solution, evaluator.shiftedSphere, 1, 1)

    # Simulated Annealing
    solution = Solution(100, 100)
    solution.start()
    optimizer = SimulatedAnnealing(100000, 0)
    optimizer.run(solution, evaluator.shiftedSphere, 1, 3, 100)


main()