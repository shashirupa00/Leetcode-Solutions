class Solution:
    def judgeSquareSum(self, c: int) -> bool:

        def binarySearch(t):

            l, r = 0, c

            while l <= r:

                mid = (l+r) // 2

                if mid**2 == t:
                    return True
                
                if mid**2 > t:
                    r = mid - 1
                
                else:
                    l = mid + 1
            
            return False
        
        a = 0

        while a * a <= c:
            b = c - (a**2)
            if binarySearch(b):
                return True
            a += 1
        
        return False



