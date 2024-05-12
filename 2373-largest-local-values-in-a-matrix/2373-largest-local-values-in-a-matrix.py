class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        
        n = len(grid)
        newMatrix = [[0 for i in range(n-2)] for i in range(n-2)]

        def findMax(i, j):

            return max(grid[i-1][j-1], grid[i-1][j], grid[i-1][j+1], grid[i][j-1], grid[i][j], grid[i][j+1], grid[i+1][j-1], grid[i+1][j], grid[i+1][j+1])

        for i in range(len(newMatrix)):
            for j in range(len(newMatrix)):
                newMatrix[i][j] = findMax(i+1, j+1)
        
        return newMatrix