class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        
        pairs.sort()
        dp = [1 for _ in pairs]
        
        for i in range(len(pairs)-2, -1, -1):
            for j in range(i+1, len(pairs)):
                if pairs[i][1] < pairs[j][0]:
                    dp[i] = max(dp[i], 1 + dp[j])

        return max(dp)