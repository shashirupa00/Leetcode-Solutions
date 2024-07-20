class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        
        rows, cols = len(rowSum), len(colSum)
        i, j = 0, 0

        res = [[0 for i in range(cols)] for j in range(rows)]

        while i < rows and j < cols:

            res[i][j] = min(rowSum[i], colSum[j])

            rowSum[i] -= res[i][j] 
            colSum[j] -= res[i][j] 

            if rowSum[i] == 0:
                i += 1
            else:
                j += 1
        
        return res