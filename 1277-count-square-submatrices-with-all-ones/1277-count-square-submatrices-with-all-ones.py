class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:

        rows, cols = len(matrix), len(matrix[0])
        res = 0

        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] and matrix[i-1][j-1] and matrix[i-1][j] and matrix[i][j-1]:
                    matrix[i][j] = 1 + min(matrix[i-1][j-1], matrix[i-1][j],  matrix[i][j-1])

        for i in range(rows):
            for j in range(cols):
                res += matrix[i][j]
        
        return res