from .optimizer import Optimizer
import random
import copy

class HillClimb(Optimizer):
    
    def hillClimb(self, solution, benchmark, p, r):
        iterations = 0
        print(solution)
        print(benchmark)
        s = copy.deepcopy(solution)
        while True:
            newSolution = copy.deepcopy(s)
            newSolution.tweak(p, r)

            print(newSolution)
            print(solution)
            x = benchmark(s)
            print(x)

            if benchmark(s) > benchmark(newSolution):
                s = solution
            iterations += 1

            if iterations >= self.iterationLimit:
                break