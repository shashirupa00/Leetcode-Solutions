class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        prefix, maxSoFar = 0, float("-inf")

        for num in nums:

            if prefix+num > 0:
                prefix += num

            else:
                prefix = 0
                        
            maxSoFar = max(maxSoFar, prefix, num) if prefix>0 else max(maxSoFar, num)


        return maxSoFar
