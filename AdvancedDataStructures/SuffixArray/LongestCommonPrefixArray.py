from AdvancedDataStructures.SuffixArray.SuffixArray import SA
class LongestCommonPrefix:
    def __init__(self, s: str) -> None:
        self.S = s
        self.suffixArray = SA(s=s)
        self.suffixArray.suffixArray()
        self.N = self.suffixArray.N
        self.P = self.suffixArray.P
        self.sa = self.suffixArray.sa

    def lcp(self):
        lcp = [0 for i in range(self.N)]
        invSuffixArray = self.P[-1]

        k = 0

        for i in range(self.N):
            if invSuffixArray[i] == self.N - 1:
                k = 0
                continue

            j = self.sa[invSuffixArray[i] + 1]

            while (i + k) < self.N and (j + k) < self.N and self.S[i + k] == self.S[j + k]:
                k += 1

            lcp[invSuffixArray[i]] = k

            if k > 0:
                k -= 1

        lcp.insert(0, 0)
        lcp.pop(-1)
        print(lcp)


s = 'banana'
lcp = LongestCommonPrefix(s=s)
lcp.lcp()
