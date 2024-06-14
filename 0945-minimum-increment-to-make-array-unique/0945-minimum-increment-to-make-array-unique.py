class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        
        nums.sort()
        res = 0
        prev = nums[0]

        for i in range(1, len(nums)):

            if nums[i] <= prev:
                res += prev + 1 - nums[i]
                prev += 1
            
            else:
                prev = nums[i]

        return res