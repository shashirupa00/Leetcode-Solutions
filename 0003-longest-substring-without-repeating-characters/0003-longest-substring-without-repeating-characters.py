class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if not s: return 0
        
        hashSet = set()
        i, j = 0, 0
        res = 1

        while j < len(s):

            while i < j and s[j] in hashSet:
                hashSet.remove(s[i])
                i += 1
            
            hashSet.add(s[j])
            
            res = max(j - i + 1, res)
            j += 1
        
        return res