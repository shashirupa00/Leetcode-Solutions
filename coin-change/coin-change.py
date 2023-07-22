class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = [float("inf") for i in range(amount+1)]
        dp[0] = 0

        for i in range(len(coins)):
            for j in range(coins[i], len(dp)):
                dp[j] = min(dp[j], 1 + dp[j - coins[i]])
        
        return dp[amount] if dp[amount] != float("inf") else -1
                