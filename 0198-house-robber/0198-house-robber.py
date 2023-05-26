class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1: return nums[0]
        if len(nums) == 2: return max(nums[0], nums[1])
        
        dp = [0 for i in range(len(nums))]
        dp[0], dp[1] = nums[0], nums[1]
        msf = nums[0]

        for i in range(2, len(nums)):
            msf = max(msf, dp[i-2])
            dp[i] = max(dp[i-1], nums[i]+msf)
            
        
        return dp[-1]
        