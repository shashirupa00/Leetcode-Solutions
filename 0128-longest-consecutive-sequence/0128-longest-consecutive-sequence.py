class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums = set(nums)
        maxRes = 0

        for num in nums:
            if num - 1 not in nums:
                cur = num
                sequence = 1
                while cur + 1 in nums:
                    cur += 1
                    sequence += 1
                maxRes = max(maxRes, sequence)
        
        return maxRes