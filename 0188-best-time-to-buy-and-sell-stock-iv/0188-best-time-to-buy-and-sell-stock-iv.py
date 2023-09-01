class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:

        dp = [[0 for i in range(len(prices))] for j in range(k+1)]
        
        for i in range(1, k+1):
            mtf = -prices[0]
            for j in range(1, len(prices)):
                dp[i][j] = max(dp[i][j-1], prices[j] + mtf)
                mtf = max(mtf, -prices[j] + dp[i-1][j])
        
        return dp[-1][-1]
