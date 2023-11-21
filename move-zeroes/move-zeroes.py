class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        if 0 in nums:
            idx = nums.index(0)

            for i in range(idx, len(nums)):
                if nums[i]:
                    nums[i], nums[idx] = nums[idx], nums[i]
                    idx += 1