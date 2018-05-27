import os
import datetime

class Log():

    def __init__(self, path, name):
        now = datetime.datetime.now()
        nowString = str(now)
        self.path = path + "/" + name + "_" + now.strftime("%Y%m%d") + ".log"

    
    def log(self, content):
        "Writes to a file. If doesn't exist, create it."
        
        mode = "w"
        
        if os.path.exists(self.path):
            mode = "a"

        file = open(self.path, mode)
        
        file.write(content)
        
        file.close()


    def logIterations(self, iterations, p, r, solution, finalSolution, benchmarkValue):
        "Logs iterations"

        self.log("\nAlgorithm ended after " + str(iterations) + " iterations." )
        self.log("\nValue of p: "+ str(p))
        self.log("\nValue of r: "+ str(r))
        self.log("\nInitial solution was: " + str(solution.content))
        self.log("\nFinal solution is: " + str(finalSolution.content))
        self.log("\nFinal benchmark is: " + str(benchmarkValue) + "\n")
