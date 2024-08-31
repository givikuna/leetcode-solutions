import re

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0: return 0
        n = int(re.sub(r'0+$', '', str(x))[::-1].replace("-", ""))
        n = -n if x < 0 else n
        if n > (2**31) - 1 or n < (-2)**31: return 0
        return n

