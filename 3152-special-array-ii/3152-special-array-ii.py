class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        
        start = 0
        arr = []
        i = 1
        res = []

        while i < len(nums):

            if nums[i] % 2 == nums[i-1] % 2:
                arr.append([start, i-1])
                start = i

            i += 1
        
        arr.append([start, i-1])

        for start, end in queries:

            l, r = 0, len(arr) - 1

            while l <= r:
                mid = (l + r) // 2

                if end > arr[mid][1]:
                    l = mid + 1
                
                elif end < arr[mid][0]:
                    r = mid - 1
                
                else:
                    if arr[mid][0] <= start <= end <= arr[mid][1]:
                        res.append(True)
                    else:
                        res.append(False)
                    break
        
        return res



        