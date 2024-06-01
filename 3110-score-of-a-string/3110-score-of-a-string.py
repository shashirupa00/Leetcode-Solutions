class Solution:
    def scoreOfString(self, s: str) -> int:
        
        res = 0

        for i in range(1, len(s)):
            l1, l2 = s[i-1], s[i]
            res += abs(ord(l1) - ord(l2))
        
        return res