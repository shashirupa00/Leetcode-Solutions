class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        
        pairs.sort()
        dp = [1 for _ in pairs]
        
        for i in range(len(pairs)-2, -1, -1):
            p1 = pairs[i]
            for j in range(i+1, len(pairs)):
                p2 = pairs[j]
                if p1[1] < p2[0]:
                    dp[i] = max(dp[i], 1 + dp[j])

        return max(dp)