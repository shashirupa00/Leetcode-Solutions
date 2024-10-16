class Solution:
    def longestPalindrome(self, s: str) -> str:

        maxLen, res = 0, ""
        
        for k in range(len(s)):

            i, j = k, k

            while i >= 0 and j < len(s) and s[i] == s[j]:

                if j - i + 1 > maxLen:
                    maxLen = j - i + 1
                    res = s[i : j + 1]
                
                i -= 1
                j += 1
        


            i, j = k, k + 1

            while i >= 0 and j < len(s) and s[i] == s[j]:

                if j - i + 1 > maxLen:
                    maxLen = j - i + 1
                    res = s[i : j + 1]
                
                i -= 1
                j += 1
        
        return res