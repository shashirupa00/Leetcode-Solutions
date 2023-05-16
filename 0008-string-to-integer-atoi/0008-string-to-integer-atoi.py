class Solution:
    def myAtoi(self, s: str) -> int:

        sign = 1
        res, i = 0, 0

        maxVal = (2**31)-1
        minVal = -(2**31)

        while i < len(s) and s[i] == ' ':
            i += 1

        if i == len(s):
            return 0
          

        if s[i] == '+' or s[i] == '-':
            if s[i] == '-':
                sign = -1
            i += 1

        while i < len(s) and s[i].isdigit():
            res = res*10 + (int(s[i]))

            if sign*res>maxVal:
                return maxVal
            elif sign*res<minVal:
                return minVal
            
            i += 1

        return sign*res 
            
