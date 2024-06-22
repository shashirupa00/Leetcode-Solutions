class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        
        lastPos = -1 
        l, r = 0, 0
        count = 0
        res = 0

        while r < len(nums):
            
            if (count == k and nums[r] % 2) or r == len(nums) - 1:

                end = r - 1 if nums[r] % 2 else r

                while count == k:

                    res += end - lastPos + 1
                    if nums[l] % 2: count -= 1
                    l += 1

            if nums[r] % 2:
                count += 1
                lastPos = r

            r += 1
        
        while count == k:

            res += 1
            if nums[l] % 2: count -= 1
            l += 1
        
        return res
