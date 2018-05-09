from .optimizer import Optimizer
import random
import copy

class HillClimb(Optimizer):
    
    def run(self):
        iterations = 0
        # newSolution = self.solution
        error = False 

        while (iterations <= self.iterationsLimit or not(error)):
            newSolution = copy.deepcopy(self.solution) 
            newSolution = self.tweak(newSolution)

            print(self.solution.content, newSolution.content)
             
            oldEval = self.evaluator.shiftedSphere(self.solution.content)

            newEval = self.evaluator.shiftedSphere(newSolution.content)

            error = abs(oldEval - newEval) <= self.error
            print(abs(oldEval - newEval) )
            print(error)
            if(self.solution.content != newSolution.content and oldEval > newEval):
                self.solution = newSolution

            iterations += 1

        return iterations

    def tweak(self, solution):
        "Tweaks the solution by decreasing a number in a random position."
        index = random.randint(0, len(solution.content) - 1)
        
        if solution.content[index] > 0:
            solution.content[index] = solution.content[index] - 1
            
        if solution.content[index] < 0:
            solution.content[index] = solution.content[index] + 1

        return solution