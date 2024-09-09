class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        hashMap = {0: 1}
        res = 0
        prefix = 0

        for i in range(len(nums)):

            prefix += nums[i]
            
            if prefix - k in hashMap:
                res += hashMap[prefix - k]
            
            hashMap[prefix] = 1 + hashMap.get(prefix, 0)
        
        return res