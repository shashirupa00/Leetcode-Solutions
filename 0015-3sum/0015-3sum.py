class Solution:
    def twoSum(self, nums, target, i , j):

        res = set()

        while i < j:
            if nums[i] + nums[j] == target:
                res.add((0-target, nums[i], nums[j]))
                i += 1
            
            elif nums[i] + nums[j] < target:
                i += 1
            
            else:
                j -= 1
    
        return res


    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        res = set()

        for i in range(len(nums)):
            target = 0 - nums[i]
            start = i+1
            ans = self.twoSum(nums, target, start , len(nums)-1)
            for t in ans:
                res.add(t)
                
        return res


        
        