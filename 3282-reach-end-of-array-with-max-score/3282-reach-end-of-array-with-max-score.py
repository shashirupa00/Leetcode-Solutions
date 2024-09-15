class Solution:
    def findMaximumScore(self, nums: List[int]) -> int:
        
        res, maxJump = 0, 0

        for jump in nums:
            res += maxJump
            maxJump = max(maxJump, jump)

        return res