class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        
        hashMap = {}
        i, j = 0, 0
        res = 0

        while j < len(s):

            hashMap[s[j]] = 1 + hashMap.get(s[j], 0)

            while len(hashMap) > k:
                hashMap[s[i]] -= 1
                if not hashMap[s[i]]: del hashMap[s[i]]
                i += 1
            
            res = max(res, j-i+1)
            j += 1
        
        return res