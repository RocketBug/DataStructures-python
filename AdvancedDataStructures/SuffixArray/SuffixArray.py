# A suffix is a substring at the end of the string with non empty characters
# A suffix array contains all the sorted suffixes contained in a string

# This function is used for transitioning from python2 to python3, need to find a better solution.
# from functools import cmp_to_key
import operator


class SA:
    S = str
    N = int

    L = []
    P = [[]]

    stp = 1
    cnt = 1

    sa = []

    def __init__(self, s: str):
        self.S = s
        self.N = len(s)
        self.P = [[0 for i in range(self.N)]]

        temp = 1
        while temp >> 1 < self.N:
            self.P.append([0 for i in range(self.N)])
            temp = temp << 1

        self.L = [0 for i in range(self.N)]
        self.sa = [0 for i in range(self.N)]

    class Entry:
        nr = []
        p = 0

        def __init__(self):
            self.nr = [0, 0]
            self.p = 0

    def suffixArray(self):
        for i in range(self.N):
            self.P[0][i] = ord(self.S[i]) - ord('$')

        while (self.cnt >> 1) < self.N:
            for i in range(self.N):
                l = self.Entry()
                l.nr[0] = self.P[self.stp - 1][i]
                l.nr[1] = self.P[self.stp - 1][i + self.cnt] if i + self.cnt < self.N else -1
                l.p = i
                self.L[i] = l

            # This type of sorting in general is know as multiple level sorting. We first sort according to the first
            # element, then the second element. In this implementation we use the attrgetter method in operator
            # module. https://docs.python.org/3/howto/sorting.html
            self.L = sorted(self.L, key=operator.attrgetter('nr'))

            # Sorts it based on the first element in the list, then if they are the same, it'll sort based on the
            # second element. func = lambda x : (x.nr[0], x.nr[1]) self.L = sorted(self.L, key=func)

            # self.L = sorted( self.L, key= cmp_to_key( lambda y, x: (1 if x.nr[1] < y.nr[1] else -1) if x.nr[0] ==
            # y.nr[0] else (1 if x.nr[0] < y.nr[0] else -1) ) )

            for i in range(self.N):
                if i > 0 and self.L[i].nr[0] == self.L[i - 1].nr[0] and self.L[i].nr[1] == self.L[i - 1].nr[1]:
                    self.P[self.stp][self.L[i].p] = self.P[self.stp][self.L[i - 1].p]

                else:
                    self.P[self.stp][self.L[i].p] = i

            self.stp += 1
            self.cnt = self.cnt << 1

        for value, i in enumerate(self.P[-1]):
            self.sa[i] = value

    def getSuffixArray(self):
        return self.sa

    def printSA(self):
        print(self.P)
        print(self.sa)
