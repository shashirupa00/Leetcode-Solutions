class Solution:
    def numSteps(self, s: str) -> int:
        
        s = s[::-1]
        num = 0
        res = 0

        for i in range(len(s)):
            if s[i] == "1":
                num += 2**i
        
        while num > 1:

            if num % 2:
                num += 1
            else:
                num = num // 2
            res += 1
        
        return res