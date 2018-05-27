from .optimizer import Optimizer
from .log import Log
import random
import copy
import datetime

class HillClimb(Optimizer):
    
    def hillClimb(self, solution, benchmark, p, r, optimal = 0):
        iterations = 0

        s = copy.deepcopy(solution)

        while True:
            newSolution = copy.deepcopy(s)
            newSolution.tweak(p, r)

            if benchmark(s) > benchmark(newSolution):
                s = newSolution
            
            iterations += 1

            if benchmark(s) == optimal or iterations >= self.iterationsLimit:
                break
        
        logger = Log("output", "hillclimb")

        logger.logIterations(iterations, p, r, solution, s, benchmark(s))