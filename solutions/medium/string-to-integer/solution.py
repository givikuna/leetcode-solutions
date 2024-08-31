class Solution:
    def myAtoi(self, s: str) -> int:
        if not s or len(s) == 0 or len(s.strip()) == 0: return 0

        sign = -1 if s.strip()[0] == "-" else 1
        n = 0
        s = s.strip()
        for i in range(0, len(s)):
            if s[i] in list("1234567890"): n = (n * 10) + int(s[i])
            elif (s[i] in list("+-")) and i == 0: continue
            else: break
        n = n * sign
        if n <= -(2 ** 31): return -(2 ** 31)
        elif n >= (2 ** 31) - 1: return (2 ** 31) - 1
        else: return n

