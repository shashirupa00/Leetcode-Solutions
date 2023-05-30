class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        coins.sort()
        dp = [float("inf") for i in range(amount+1)]

        dp[0] = 0

        for i in range(1, amount+1):
            for j in range(len(coins)):

                temp = i - coins[j]

                if temp == 0: dp[i] = 1
                
                elif temp < 0: break
                
                dp[i] = min(1 + dp[temp], dp[i])
        
        return -1 if dp[-1] == float("inf") else dp[-1]
                

        