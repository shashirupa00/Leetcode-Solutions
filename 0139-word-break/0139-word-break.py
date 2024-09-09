class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        dp = [False for i in range(len(s) + 1)]
        dp[-1] = True

        for i in range(len(s) - 1, -1, -1):
            for word in wordDict:
                n = len(word)
                cur = s[i : i + n]
                if s[i : i + n] == word:
                    dp[i] = dp[i + n]
                    if dp[i]:
                        break
        
        return dp[0]