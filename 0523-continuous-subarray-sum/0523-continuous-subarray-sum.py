class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:

        hashMap = {0:0}
        prefixSum = 0

        for i in range(len(nums)):
            prefixSum += nums[i]
            remainder = prefixSum % k

            if remainder not in hashMap:
                hashMap[remainder] = i+1

            elif hashMap[remainder] < i:
                return True
                       
        return False


