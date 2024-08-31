from typing import List

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s): return s
        arr: List[str] = ["" for row in range(numRows)]
        i: int = 0
        starter: int = numRows
        for c in s:
            if starter == numRows:
                arr[i] += c
                i += 1
                if i == numRows:
                    starter -= 1
                    i = starter
            else:
                if starter == 1:
                    i = 1
                    starter = numRows
                    arr[0] += c
                else:
                    arr[starter - 1] += c
                    starter -= 1
        return ''.join(arr)
        """
        arr: List[str] = ["" for n in range(numRows)]
        i: int = 0
        for c in s:
            if i < numRows:
                arr[i] += c
                i += 1
            else:
                arr[math.floor(numRows / 2)] += c
                i = 0
        return ''.join(arr)
        """
