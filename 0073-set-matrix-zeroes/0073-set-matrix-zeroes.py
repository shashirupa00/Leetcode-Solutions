class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        def setZero_helper(row, col):
            for c in range(len(matrix[0])):
                if matrix[row][c] != 0:
                    matrix[row][c] = "#" 
            for r in range(len(matrix)):
                if matrix[r][col] != 0:
                    matrix[r][col] = "#" 

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    setZero_helper(row, col)
        
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == "#":
                    matrix[row][col] = 0