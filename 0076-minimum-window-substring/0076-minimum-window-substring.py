class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(s) < len(t): return ""

        i, j = 0, 0
        res = ""
        minLen = float("inf")
        sMap, tMap = {}, {}

        for char in t:
            tMap[char] = 1 + tMap.get(char, 0)

        have, need = 0, len(tMap)

        while j < len(s):
            char = s[j]

            if char in tMap:
                sMap[char] = 1 + sMap.get(char, 0)

                if sMap[char] == tMap[char]:
                    have += 1

            while have == need:

                if minLen > (j-i+1):
                    minLen = j-i+1
                    res = s[i:j+1]

                if s[i] in sMap:
                    sMap[s[i]] -= 1

                    if sMap[s[i]] < tMap[s[i]]:
                        have -= 1

                i += 1
            j += 1

        return res                    

        
         