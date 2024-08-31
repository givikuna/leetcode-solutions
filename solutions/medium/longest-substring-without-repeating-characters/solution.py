class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        current= ""
        prev = ""
        i = 0

        for i in range(len(s)):
            if s[i] in current:
                if len(current) >= len(prev): prev = current
                current = current[current.index(s[i], 0)+1:len(current)] + s[i]
            else: current += s[i]
        if len(current) >= len(prev): return len(current)
        return len(prev)
