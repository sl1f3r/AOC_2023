class Solution: 
    def __init__(self):
        self.input = '/Users/thom/Code/AOC_2023/day1.txt'
        self.total = 0

    def calcvalue(self):
        file = open(self.input, 'r')

        for line in file: 
            numarray = []
            val = 0
            for character in line: 
                if isinstance(character, int):
                    numarray.append(character)
            
            if len(numarray) == 1: 
                strval = str(numarray[0]) + str(numarray[0])
                val = int(strval)
            elif len(numarray) > 1: 
                strval = str(numarray[0]) + str(numarray[-1])
                val = int(strval)
            
            self.total += val


        return self.total
    
sol = Solution()
print(sol.calcvalue())