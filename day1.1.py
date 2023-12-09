import collections
import re

class Solution: 
    def __init__(self):
        self.input = '/Users/thom/Code/AOC_2023/day1.txt'
        self.total = 0
        self.map = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 
                    'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10}

    def calcvalue(self, line): # calculates the numerical value of a line
        val = 0
        numdict = {}
        for i in range(len(line)): 
            if line[i].isnumeric(): # check which characters in that line are numbers
                numdict[i] = line[i]
        
        for key in self.map.keys():
            instances = [m.start() for m in re.finditer(key, line)]
            if instances:
                for ins in instances: 
                    numdict[ins] = self.map[key]

        od = collections.OrderedDict(sorted(numdict.items()))
        strval = str(list(od.items())[0][1]) + str(list(od.items())[-1][1])
        val = int(strval)

        return val

    def read_file(self): 
        file = open(self.input)
        for line in file: 
            value = self.calcvalue(line) # iterate through file, get the value of each line, and add up
            self.total += value

        return self.total
    
sol = Solution()
print(sol.read_file())