class SimpleSuffixArray:

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

s = 'banana'
simpleSuffixArray = SimpleSuffixArray(s=s)
simpleSuffixArray.printSA()
