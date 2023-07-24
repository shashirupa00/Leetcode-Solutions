class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:

        hashSet = set()

        for i in range(len(s)):
            if (i+k-1) < len(s):
                hashSet.add(s[i:i+k])
        
        return len(hashSet) == pow(2, k)