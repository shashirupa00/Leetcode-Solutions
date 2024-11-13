class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        
        nums.sort()
        res = 0

        l, r = 0, len(nums) - 1

        while l < r:

            curSum = nums[l] + nums[r]

            if curSum <= upper:
                res += r - l
                l += 1

            else:
                r -= 1
        
        l, r = 0, len(nums) - 1

        while l < r:

            curSum = nums[l] + nums[r]

            if curSum < lower:
                res -= r - l
                l += 1

            else:
                r -= 1
        
        return res

        