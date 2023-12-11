import re

class Solution: 
    def __init__(self):
        self.input = '/Users/thom/Code/AOC_2023/day2.txt'
        self.total = 0
        self.game = 1
        self.map = {'red': 12, 'green': 13, 'blue': 14}

    def get_values(self, color, line): 
        instances = [m.start() for m in re.finditer(color, line)] # get starting index for each occurance of the color
        values = []# total array to keep track of values
        for i in instances: 
            numstring = "" # string to track number
            fo_befo = i - 4
            subslice = line[fo_befo: i]
            for item in subslice: 
                if item.isnumeric(): numstring = numstring + str(item)

            values.append(int(numstring))

        return values

    
    def check_possibility(self, line): 
        possible = True

        greenvals = self.get_values('green', line)# figure out green values
        redvals = self.get_values('red', line)# figure out red values
        bluevals = self.get_values('blue', line) # figure out blue values

        for g in greenvals:
            if g > self.map['green']: possible = False
        for r in redvals: 
            if r > self.map['red']: possible = False
        for b in bluevals: 
            if b > self.map['blue']: possible = False

        # compare and decide
        if possible: self.total += self.game

        self.game += 1
                


    def solve(self):
        file = open(self.input)
        for line in file: 
            self.check_possibility(line)
        
        return self.total

sol = Solution()
print(sol.solve())