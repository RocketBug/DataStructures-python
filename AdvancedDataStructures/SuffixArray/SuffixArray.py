# A suffix is a substring at the end of the string with non empty characters
# A suffix array contains all the sorted suffixes contained in a string

class SuffixArray:

    suffixArray = []
    suffixArrayIndex = []

    def __init__(self, s: str):
        for i in range(len(s)):
            self.suffixArray.append((i, s[i:]))

        self.suffixArray.sort(key= lambda x : x[1])

        for i in self.suffixArray:
            self.suffixArrayIndex.append(i[0])

    def printSA(self):
        print(self.suffixArray)
        print(self.suffixArrayIndex)


class SA:
    S = str
    N = int

    L = []
    P = [[]]
    
    stp = 1
    cnt = 1

    sa = []

    def __init__(self, s:str):
        self.S = s
        self.N = len(s)
        self.P = [[0 for i in range(self.N)]]
        
        
        temp = 1 
        while temp < self.N:
            self.P.append([0 for i in range(self.N)])
            temp = temp << 1

        self.L = [0 for i in range(self.N)]

    class Entry:
        nr = []
        p = 0
        def __init__(self):
            self.nr = [0,0]
            self.p = 0

    def suffixArray(self):
        for i in range(self.N):
            self.P[0][i] = ord(self.S[i])-ord('a')

        while self.cnt < self.N:

            for i in range(self.N):
                l = self.Entry()
                l.nr[0] = 'apple'
                l.nr[0] = self.P[self.stp - 1][i]

                l.nr[1] = self.P[self.stp - 1][i + self.cnt] if i + self.cnt < self.N else -1

                l.p = i

                self.L[i] = l
                

            self.L.sort(key= lambda l : l.nr[0])
            
            
            for i in range(self.N):
                if i > 0 and self.L[i].nr[0] == self.L[i-1].nr[0] and self.L[i].nr[1] == self.L[i-1].nr[1]:
                    self.P[self.stp][self.L[i].p] = self.P[self.stp][self.L[i-1].p]

                else:
                    self.P[self.stp][self.L[i].p] = i    
                
            self.stp += 1
            self.cnt = self.cnt << 1

        for e, i in enumerate(self.P[-1]):

            self.sa.insert(i, e)
            
    def printSA(self):
        print(self.P)
        print(self.sa)


s = 'camel'
sa = SA(s)
sa.suffixArray()
sa.printSA()

