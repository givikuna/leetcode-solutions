from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s = ''
        minimum_length = min(list(map(len, strs)))
        for i in range(0, minimum_length):
            if len(list(filter(lambda x: x != strs[0][i], list(map(lambda x: x[i], strs))))) == 0:
                s += strs[0][i]
            else:
                break
        return s

