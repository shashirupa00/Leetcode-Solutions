class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:

        dp = [0 for _ in nums]
        
        for i in range(len(nums) - 2, -1, -1):
            for j in range(i+1, len(nums)):
                if abs(nums[i] - nums[j]) <= target:
                    if dp[j] != 0 or j == len(nums) - 1:
                        dp[i] = max(dp[i], 1 + dp[j])
        
        return dp[0] if dp[0] else -1
