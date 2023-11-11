class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        numSet = set(nums)
        numSet = sorted(list(numSet))

        for i in range(len(numSet)):
            nums[i] = numSet[i]
        
        return len(numSet)
