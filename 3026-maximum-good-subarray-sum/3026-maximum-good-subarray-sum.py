class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:

        n = len(nums)
        prefix_sum = [0] * (n + 1)
        for i in range(1, n + 1):
            prefix_sum[i] = prefix_sum[i-1] + nums[i-1]
        
        seen = {}
        max_sum = float('-inf')
        
        for i in range(n):
            target1, target2 = nums[i] - k, nums[i] + k
            
            if target1 in seen:
                max_sum = max(max_sum, prefix_sum[i+1] - seen[target1])
            if target2 in seen:
                max_sum = max(max_sum, prefix_sum[i+1] - seen[target2])
            
            if nums[i] not in seen or prefix_sum[i] < seen[nums[i]]:
                seen[nums[i]] = prefix_sum[i]
        
        return max_sum if max_sum != float('-inf') else 0