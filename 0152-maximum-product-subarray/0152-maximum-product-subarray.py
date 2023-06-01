class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        res = max(nums)
        minSoFar, maxSoFar = nums[0], nums[0]

        for i in range(1, len(nums)):

            temp = maxSoFar * nums[i]
            maxSoFar = max(nums[i]*maxSoFar, nums[i]*minSoFar, nums[i])
            minSoFar = min(temp, nums[i]*minSoFar, nums[i])

            res = max(res, maxSoFar, minSoFar)
        
        return res