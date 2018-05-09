import math

class Evaluator:

    def __init__(self, error = 1):
        self.error = error
    
    
    def shiftedSphere(self, solution, bias = 0 ):
        "Shifted Sphere function for benchmarking"
        sum = 0
        for x in range(0, len(solution)):
            sum += solution[x] * solution[x]
        sum += bias
        return sum


    def shiftedRosenbrock(self, solution, bias = 0 ):
        "Shifted Rosenbrock's function for benchmarking."

        sum = 0
        for x in range(0, len(solution) - 1):
            sum += (100 * ((solution[x]**2) - solution[x + 1])**2) + (solution[x] - 1)**2

        sum += bias

        return sum

    
    def shiftedRastrign(self, solution, bias = 0):
        "Shifted Rosenbrock's function for benchmarking."

        sum = 0
        for x in range(0, len(solution)):
            sum += solution[x]**2 - (10 * math.cos(2 * math.pi * solution[x]) + 10)
        
        sum += bias

        return sum        
