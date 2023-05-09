class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:

        if s == "-":
            return ""

        if len(s) == 1:
            return s.capitalize()

        s = s[::-1]
        res = ""

        for i in range(len(s)):
            if s[i].isalnum():
                res += s[i].capitalize()
                
        start, ans = 0, ""
        for i in range(len(res)):
            x = i+1
            if x % k == 0:
                if ans == "":
                    ans += res[start:i+1]
                else:
                    ans += "-" + res[start:i+1]
                start = i+1
        
        if start < len(res):
            ans += "-" + res[start:]

        return ans[::-1]


            


            





        