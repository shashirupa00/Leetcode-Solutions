class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        rows, cols = len(grid), len(grid[0])

        dp = [[0 for i in range(cols)] for j in range(rows)]
        dp[0][0] = grid[0][0]

        for i in range(rows):
            for j in range(cols):

                if (i, j) != (0, 0):
                    nei1, nei2 = (dp[i - 1][j] if i - 1 >= 0 else float("inf")), (dp[i][j - 1] if j - 1 >= 0 else float("inf"))
                    dp[i][j] = grid[i][j] + min(nei1, nei2)
        
        print(dp)
        return dp[-1][-1]