from .optimizer import Optimizer
import copy
import math
import random
from .log import Log

class SimulatedAnnealing(Optimizer):
    "Optimization Algorithms: Simulated Annealing"

    def __init__(self, iterationsLimit, schedule):
        self.iterationsLimit = iterationsLimit
        self.schedule = schedule
    
    def run(self, solution, benchmark, p, r, t, optimal = 0):
        iterations = 0

        s = copy.deepcopy(solution)
        best = copy.deepcopy(s)

        while True:
            newSolution = copy.deepcopy(s)
            newSolution.tweak(p, r)

            benchOld = benchmark(s)
            benchNew = benchmark(newSolution)
            
            e = math.pow(math.e, (benchNew - benchOld)/t)
            
            if benchOld < benchNew or random.random() < e:
                s = newSolution
            
            t -= self.schedule

            if benchmark(s) < benchmark(best):
                best = copy.deepcopy(s)

            iterations += 1

            if iterations == self.iterationsLimit or t <= 0:
                break
        
        logger = Log("output", "simAnnealing")
        logger.logIterations(iterations, p, r, solution, best, benchmark(best))






            
