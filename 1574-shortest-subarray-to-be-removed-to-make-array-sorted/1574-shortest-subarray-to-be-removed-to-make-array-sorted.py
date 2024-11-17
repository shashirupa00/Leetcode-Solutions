class Solution:
    def findLengthOfShortestSubarray(self, nums: List[int]) -> int:
        
        #Find the breaking point

        arr1 = []
        breakPoint = 0

        for i, num in enumerate(nums):
            if arr1 and num < arr1[-1][0]:
                break
            arr1.append((num, i))
            breakPoint = i

        #Find the second increasing array
        arr2 = []

        for i in range(breakPoint + 1, len(nums)):
            
            if arr2 and nums[i] < arr2[-1][0]:
                arr2 = []

            arr2.append((nums[i], i))

        if not arr2: return 0
        
        res = min(len(nums) - len(arr1), len(nums) - len(arr2))
        
        for i in range(len(arr2)):
            idx = bisect.bisect_right(arr1, arr2[i])
            if idx:
                res = min(res, arr2[i][1] - arr1[idx - 1][1] - 1)
        
        return res

