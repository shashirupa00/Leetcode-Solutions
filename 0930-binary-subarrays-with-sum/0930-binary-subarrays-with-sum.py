class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        
        hashMap = {0: 1}
        prefix = 0
        res = 0

        for num in nums:

            prefix += num

            if prefix - goal in hashMap:
                res += hashMap[prefix - goal]
            
            hashMap[prefix] = 1 + hashMap.get(prefix, 0)
        
        return res