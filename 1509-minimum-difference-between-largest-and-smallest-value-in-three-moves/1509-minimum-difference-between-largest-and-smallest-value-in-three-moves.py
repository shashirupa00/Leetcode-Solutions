class Solution:
    def minDifference(self, nums: List[int]) -> int:
        
        if len(nums) <= 4:
            return 0

        nums.sort()

        # [0, 1, 2, 3, 4]
        #  i  j    

        i, j = 0, -4

        res = float("inf")

        while i < 4 and j < 0:

            res = min(res, nums[j] - nums[i])
            j += 1
            i += 1
        
        return res