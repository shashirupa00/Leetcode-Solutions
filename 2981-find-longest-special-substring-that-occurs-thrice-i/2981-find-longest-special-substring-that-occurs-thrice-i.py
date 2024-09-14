class Solution:
    def maximumLength(self, s: str) -> int:
        
        hashMap = defaultdict(int)

        for r in range(len(s)):
            l = r
            
            while r < len(s) and s[l] == s[r]:
                r += 1
                hashMap[s[l : r]] += 1

        res = -1

        for k in hashMap:
            if hashMap[k] >= 3:
                res = max(res, len(k))
        
        return res