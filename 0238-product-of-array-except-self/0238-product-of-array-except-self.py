class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
         
        pre, post = 1, nums[-1]
        res = [1 for _ in range(len(nums))]

        for i in range(1, len(nums)):
            res[i] = pre * nums[i-1]
            pre *= nums[i-1]
        
        for i in range(len(nums)-2, -1, -1):
            res[i] = res[i] * post
            post *= nums[i]
            

        return res
        



        

        

        
    
