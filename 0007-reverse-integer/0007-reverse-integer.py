class Solution:
    def reverse(self, x: int) -> int:

        num, sign = 0, 1
        INT_MIN, INT_MAX = -(2**31), (2**31-1)

        if x<0:
            sign = -1
            x *= -1

        while x > 0:
            temp = x % 10
            x = x//10
            num = num*10 + temp
    
            if sign*num > INT_MAX or sign*num < INT_MIN:
                return 0
        
        return sign*num


        
        


        
