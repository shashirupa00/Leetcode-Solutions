class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        prefix, maxSoFar = 0, float("-inf")

        for num in nums:        
            prefix += num
            maxSoFar = max(maxSoFar, prefix)

            if prefix<0:
                prefix = 0
                        
        return maxSoFar
