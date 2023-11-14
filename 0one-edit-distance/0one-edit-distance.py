class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:

        if abs(len(s) - len(t)) > 1 or s == t:
            return False

        if len(s) > len(t):
            s, t = t, s

        change = 0
        
        if len(s) == len(t):

            for sChar, tChar in zip(s, t):

                if sChar != tChar :
                    if change:
                        return False
                    else:
                        change = 1

        else:
            i, j = 0, 0
            while i < len(s):
                
                if s[i] == t[j]:
                    i += 1
                    j += 1
                
                else:
                    if change:
                        return False
                    else:
                        j += 1
                        change = 1
        
        return True