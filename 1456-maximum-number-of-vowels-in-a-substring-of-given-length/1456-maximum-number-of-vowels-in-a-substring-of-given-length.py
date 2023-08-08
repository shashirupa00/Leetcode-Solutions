class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        l, r = 0 , k-1
        curCount, maxCount = 0, 0
        vowels = {'a', 'e', 'i', 'o', 'u'}

        for i in range(k):
            if s[i] in vowels:
                curCount +=1
        
        maxCount = curCount

        while r < len(s):

            if s[l] in vowels:
                curCount -= 1
            
            l += 1
            r += 1

            if r < len(s)and s[r] in vowels:
                curCount += 1
            
            maxCount = max(maxCount, curCount)

        return maxCount