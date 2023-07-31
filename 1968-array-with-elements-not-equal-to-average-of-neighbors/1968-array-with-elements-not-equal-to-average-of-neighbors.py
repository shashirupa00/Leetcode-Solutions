class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]: 

        for i in range(1, len(nums)):
            if i%2:
                if nums[i] < nums[i-1]:
                    nums[i], nums[i-1] = nums[i-1], nums[i]
            
            else:
                if nums[i] > nums[i-1]:
                    nums[i], nums[i-1] = nums[i-1], nums[i]
        
        return nums

