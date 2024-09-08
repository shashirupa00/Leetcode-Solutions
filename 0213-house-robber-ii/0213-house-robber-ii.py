class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) <= 2:
            return max(nums)

        def robHouse(arr):
        
            dp = [0 for i in range(len(arr))]
            dp[0], dp[1] = arr[0], max(arr[0], arr[1])

            for i in range(2, len(arr)):
                dp[i] = max(dp[i - 1], arr[i] + dp[i - 2])
            
            return max(dp)
        
        return max(robHouse(nums[0:len(nums) -1]), robHouse(nums[1:]))