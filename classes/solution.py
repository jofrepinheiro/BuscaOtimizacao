import random

class Solution:
   
    def __init__(self, limit, dimension):
        self.limit = limit
        self.dimension = dimension
        self.content = []

    def __len__(self):
        return len(self.content)

    def start(self):
        for x in range(0, self.dimension):
            self.content.append(random.randint(-self.limit, self.limit))


    def print(self):
        print(*self.content, sep =  ', ')

    def tweak(self, p, r):
        """Bounded Uniform Convolution algorithm for tweaking a solution
        p: noise probability
        r: noise range"""
        for i in range(-self.dimension, self.dimension):
            if p > random.random():
                tweakedValue = 0
                while True:
                    n = random.randint(-r, r)
                    tweakedValue = self.content[i] + n
                    
                    if -self.limit <= tweakedValue and tweakedValue <= self.limit:
                        break
                self.content[i] = tweakedValue
        return self.content
            
                
                    


