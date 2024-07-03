# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        
        rows, cols = binaryMatrix.dimensions()
        res = float("inf")

        def binarySearch(i):

            l, r = 0, cols - 1

            while l <= r:

                mid = (l + r) // 2

                if binaryMatrix.get(i, mid):
                    r = mid - 1
                
                else:
                    l = mid + 1
            
            return l
            
        for i in range(rows):
            if binaryMatrix.get(i, cols - 1):
                res = min(res, binarySearch(i))
        
        return res if res != float("inf") else -1