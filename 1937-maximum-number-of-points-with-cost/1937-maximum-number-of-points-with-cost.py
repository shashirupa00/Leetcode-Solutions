class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:

        rows, cols = len(points), len(points[0])
        dp = [[0 for i in range(cols)] for j in range(rows)]
        dp[0] = points[0][:]

        for i in range(1, rows):
            
            left = [0] * (cols)
            right = [0] * (cols)
            left[0], right[-1] = dp[i-1][0], dp[i-1][-1]

            for j in range(1, cols):
                left[j] = max(dp[i - 1][j], left[j - 1] - 1)
            
            for j in range(cols-2, -1, -1):
                right[j] = max(dp[i - 1][j], right[j + 1] - 1)
            
            for j in range(cols):
                dp[i][j] = points[i][j] + max(left[j], right[j])
        
        return max(dp[-1])
            

            
        
        return max(dp[-1])