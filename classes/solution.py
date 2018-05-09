import random

class Solution:
   
    def __init__(self, limit, dimension):
        self.limit = limit
        self.dimension = dimension
        self.content = []


    def start(self):
        for x in range(0, self.dimension):
            self.content.append(random.randint(-self.limit, self.limit))


    def print(self):
        print(*self.content, sep =  ', ')