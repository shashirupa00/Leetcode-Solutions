class Solution:
    def numDecodings(self, s: str) -> int:

        if s[0] == '0':
            return 0

        hashSet = set([str(i) for i in range(1, 27)])

        dp = [0 for i in range(len(s) + 1)]
        dp[0], dp[1] = 1, 1

        for i in range(2, len(s) + 1):

            if s[i - 1] in hashSet:
                dp[i] += dp[i-1]
            
            if s[i - 2] + s[i - 1] in hashSet:
                dp[i] += dp[i-2]

        return dp[-1]