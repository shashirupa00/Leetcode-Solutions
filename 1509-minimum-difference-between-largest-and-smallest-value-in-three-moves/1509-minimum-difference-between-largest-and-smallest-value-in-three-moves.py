class Solution:
    def minDifference(self, nums: List[int]) -> int:
        
        if len(nums) <= 4:
            return 0

        nums.sort()
        res = float("inf")

        print(nums)

        i, j = 0 , -4

        while i < 4 and j < 0:
            res = min(res, abs(nums[i] - nums[j]))
            i += 1
            j += 1

        return res