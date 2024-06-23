class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:

        rows, cols = len(grid), len(grid[0])
        
        topRow, bottomRow = float("inf"), float("-inf")
        leftCol, rightCol = float("inf"), float("-inf")


        for i in range(rows):
            for j in range(cols):
                if grid[i][j]:
                    topRow, bottomRow = min(topRow, i), max(bottomRow, i)
                    leftCol, rightCol= min(leftCol, j), max(rightCol, j)


        return (bottomRow - topRow + 1) * (rightCol - leftCol + 1)