class Solution: 
    def __init__(self):
        self.input = '/Users/thom/Code/AOC_2023/day1.txt'
        self.total = 0
        self.map = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 
                    'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10}

    def calcvalue(self, line): # calculates the numerical value of a line
        value = 0

        
        return value

    def read_file(self): 
        file = open(self.input)
        for line in file: 
            value = self.calcvalue(line)
            self.total += value

        return self.total

        
            

        