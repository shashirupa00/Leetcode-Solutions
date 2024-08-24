class Solution:
    def minSwaps(self, nums: List[int]) -> int:

        totalOnes = sum(nums)
        nums.extend(nums)
        l, r = 0, totalOnes - 1
        curSum = sum(nums[l: r+1])
        res = float("inf")

        if totalOnes == 0:
            return 0

        while r < len(nums):

            res = min(res, r - l + 1 - curSum)
            curSum -= nums[l]

            l += 1
            r += 1

            if r < len(nums):
                curSum += nums[r]
        
        return res