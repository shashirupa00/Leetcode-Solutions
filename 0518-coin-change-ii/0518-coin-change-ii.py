class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        dp = [0 for i in range(amount+1)]
        dp[0] = 1

        for i in range(len(coins)):
            for j in range(1, amount+1):          
                x = 0 if j - coins[i] < 0 else dp[j - coins[i]]
                dp[j] = dp[j] + x
        
        return dp[-1]
            




    



        