class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        dp = [0 for i in range(len(prices))]

        minSoFar = prices[0]

        for i in range(1, len(prices)):
            
            profit = prices[i] - minSoFar
            dp[i] = max(dp[i-1], profit)
            minSoFar = min(minSoFar, prices[i])
        
        return dp[-1]
        