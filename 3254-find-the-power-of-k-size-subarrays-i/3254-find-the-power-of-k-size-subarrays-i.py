class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        
        '''
        [1,2,3,4,3,2,5]
         i   j
         [(a[j] or -1)] * 5

         set([4, 5, 6])

        '''

        res = []
        l, r = 0, k - 1

        def helper(nums):

            for i in range(1, len(nums)):
                if nums[i] - nums[i-1] != 1:
                    return False
            
            return True
        
        while r < len(nums):
            
            if helper(nums[l:r+1]):
                res.append(nums[r])
            
            else:
                res.append(-1)

            l += 1
            r += 1

        return res