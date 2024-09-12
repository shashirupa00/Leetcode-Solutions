class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        dp = defaultdict(int)

        def backTrack(i, state):
            
            if i >= len(prices):
                return 0
            
            if (i, state) in dp:
                return dp[(i, state)]
            
            s1, s2 = 0, 0

            #buy
            if state == 'buy':
                s1 = max(backTrack(i + 1, 'sell') - prices[i], backTrack(i + 1, state))

            #sell
            if state == 'sell':
                s2 = max(backTrack(i + 2, 'buy') + prices[i], backTrack(i + 1, state))

            dp[(i, state)] = max(s1, s2)

            return dp[(i, state)]
        
        return backTrack(0, 'buy')