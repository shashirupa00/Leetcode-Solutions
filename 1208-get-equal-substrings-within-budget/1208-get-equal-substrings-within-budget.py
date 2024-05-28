class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        
        arr = [abs(ord(s[i]) - ord(t[i])) for i in range(len(s))]
        i, j = 0, 0
        curSum = 0
        res = 0

        while j < len(s):

            curSum += arr[j]

            while i < len(s) and curSum > maxCost:
                curSum -= arr[i]
                i += 1
            
            res = max(res, j-i+1)
            j += 1
        
        return res