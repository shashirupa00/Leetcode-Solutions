class Solution:
    def maximumTotalCost(self, nums: List[int]) -> int:
        
        if len(nums) == 1: return nums[0]

        prevState = [nums[0] + nums[1], nums[0] - nums[1]]

        if len(nums) == 2: return max(prevState)

        curState = [0, 0]

        for i in range(2, len(nums)):
            curState[0] = max(prevState) + nums[i]
            curState[1] = prevState[0] - nums[i]
            prevState = curState[:]
        
        return max(curState)
