class Solution:
    def numSquares(self, n: int) -> int: 

        dp = [float("inf") for _ in range(n+1)]
        dp[0], i = 0, 1
        squares = []

        while i*i <= n:
            squares.append(i*i)
            i += 1
        
        for i in range(n+1):
            for j in range(len(squares)):

                if i < squares[j]: break

                temp = i-squares[j]
                dp[i] = min(dp[i], dp[temp]+1)
        
        return dp[-1]


        


                