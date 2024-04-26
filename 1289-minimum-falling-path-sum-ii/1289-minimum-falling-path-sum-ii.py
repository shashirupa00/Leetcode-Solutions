class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        
        rows, cols = len(grid), len(grid[0])

        dp = [[0 for j in range(cols)] for i in range(rows)]
        dp[0] = grid[0]

        for i in range(1, rows):
            for j in range(cols):
                left = min(dp[i-1][:j]) if j != 0 else float("inf")
                right = min(dp[i-1][j+1:]) if j != cols - 1 else float("inf")
                dp[i][j] = grid[i][j] + min(left, right)
        
        return min(dp[-1])


