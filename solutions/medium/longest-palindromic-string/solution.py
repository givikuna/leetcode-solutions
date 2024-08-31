class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s == s[::-1]: return s
        possibilities = []
        cl = len(s) - 1 #current
        count = 0
        while True:
            i = 0
            for i in range(len(s)-cl+1): possibilities.append(s[i:i+cl])
            for p in possibilities:
                if p == p[::-1]: return p
            cl -= 1
            possibilities = []
            count += 1
            if count == len(s): break
        return s[0]

