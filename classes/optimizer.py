class Optimizer():

    def __init__(self, solution, evaluator, error, iterationsLimit = 100 ):
        self.error = error
        self.solution = solution
        self.iterationsLimit = iterationsLimit
        self.evaluator = evaluator
        self.newSolution = solution
        
    def tweak(self):
        pass

    def run(self):
        pass