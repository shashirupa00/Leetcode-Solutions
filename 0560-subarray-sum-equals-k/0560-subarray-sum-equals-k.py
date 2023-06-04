class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        hashMap = {0:1}
        prefixSum = 0
        res = 0

        for i in range(len(nums)):
            prefixSum += nums[i]

            if prefixSum - k in hashMap:
                res += hashMap[prefixSum-k]
                
            hashMap[prefixSum] = 1 + hashMap.get(prefixSum, 0)
        
        return res