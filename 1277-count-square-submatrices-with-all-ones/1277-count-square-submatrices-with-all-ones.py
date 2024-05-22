class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:

        rows, cols = len(matrix), len(matrix[0])
        res = 0

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j]: 
                    if i > 0 and j > 0 and matrix[i-1][j-1] and matrix[i-1][j] and matrix[i][j-1]:
                        matrix[i][j] = 1 + min(matrix[i-1][j-1], matrix[i-1][j],  matrix[i][j-1])          
                    res += matrix[i][j]
       
        return res