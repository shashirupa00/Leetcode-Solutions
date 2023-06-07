class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = j = len(nums)-1


        while i>0:
            if nums[i-1] < nums[i]:

                while j >= 0 and nums[j] <= nums[i-1]:
                    j -= 1
                
                nums[i-1], nums[j] = nums[j], nums[i-1]
                break
            i -= 1

        nums[i:] = nums[i:][::-1]
            
            
        
       



           