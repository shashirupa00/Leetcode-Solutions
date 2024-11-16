class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:

        if k == 1:
            return nums

        res = [-1 for _ in range(len(nums) - k + 1)]
        count = 1

        for i in range(len(nums) - 1):
            
            if nums[i + 1] - nums[i] == 1:
                count = count + 1 
            
            else:
                count = 1

            if count >= k:
                res[i - k + 2] = nums[i + 1]
        
        return res