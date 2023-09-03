class Solution:
    def numTrees(self, n: int) -> int:
        
        dp = {0:1}
        res = 0

        def dfs(n):

            nonlocal res

            if n in dp:
                return dp[n]

            for i in range(1,n+1):
                res += dfs(i-1) * dfs(n-i)
            
            dp[n] = res
            return res
        
        return dfs(n)
        