from AdvancedDataStructures.SuffixArray.LongestCommonPrefixArray import LongestCommonPrefix


class UniqueSubStrings:

    def __init__(self, s:str) -> None:
        self.S = s
        self.N = len(s)
        self.number_of_substrings = (self.N*(self.N+1)) // 2

    def get_number_of_substrings(self):
        return self.number_of_substrings

    def number_of_unique_substrings(self) -> int:
        longest_common_prefix = LongestCommonPrefix(s=self.S)
        lcp_array = longest_common_prefix.lcp()
        sum_lcp_array = sum(lcp_array)
        number_of_substrings = self.get_number_of_substrings()
        return  number_of_substrings - sum_lcp_array

s = "AZAZA"
us = UniqueSubStrings(s=s)
print(us.number_of_unique_substrings())