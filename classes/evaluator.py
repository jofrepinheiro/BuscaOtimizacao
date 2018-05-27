import math

class Evaluator:

    def __init__(self, error = 1):
        self.error = error
    
    
    def shiftedSphere(self, solution, bias = 0 ):
        "Shifted Sphere function for benchmarking"
        sum = 0
        for x in range(0, len(solution)):
            sum += solution.content[x] * solution.content[x]
        sum += bias
        return sum


    def shiftedRosenbrock(self, solution, bias = 0 ):
        "Shifted Rosenbrock's function for benchmarking"

        sum = 0
        for x in range(0, len(solution) - 2):
            sum += (100 * ((solution.content[x]**2) - solution.content[x + 1])**2) + (solution.content[x] - 1)**2

        sum += bias

        return sum

    
    def shiftedRastrign(self, solution, bias = 0):
        "Shifted Rosenbrock's function for benchmarking"

        sum = 0
        for x in range(0, len(solution) - 1):
            sum += solution.content[x]**2 - (10 * math.cos(2 * math.pi * solution.content[x]) + 10)
        
        sum += bias

        return sum        


    def shiftedGriewank(self, solution, bias = 0):
        "Shifted Griewank's function for benchmarking"

        sum = 0
        product = 1

        for x in range(0, len(solution) - 1):
            sum += solution.content[x]**2 / 4000
        
        for y in range(0, len(solution.content) - 1):
            product *= math.cos(solution.content[y] / math.sqrt(y))
        
        return sum - product + 1 + bias
            