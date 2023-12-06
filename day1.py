class Solution: 
    def __init__(self):
        self.input = '/Users/thom/Code/AOC_2023/day1.txt'
        self.total = 0

    def calcvalue(self):
        file = open(self.input) # read file 

        for line in file: # line by line through file
            numarray = []
            val = 0
            for character in line: 
                if character.isnumeric(): # check which characters in that line are numbers
                    print(character)
                    numarray.append(character) # add to array per line
            
            if len(numarray) == 1: # if length is one, that num is first and last
                strval = str(numarray[0]) + str(numarray[0])
                val = int(strval)
            elif len(numarray) > 1: # if not, add the first and last
                strval = str(numarray[0]) + str(numarray[-1])
                val = int(strval)
            
            self.total += val # add to total

        return self.total

    # PART TWO
    def calcvalue_words(self): 
        return 0

        
    
sol = Solution()
print(sol.calcvalue())