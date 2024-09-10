class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        totalSum = sum(nums)
        
        if totalSum % 2:
            return False

        target = totalSum // 2
        dp = {}

        def backTrack(i, sumSoFar):
            
            if sumSoFar > target or i >= len(nums):
                return False
            
            if sumSoFar == target:
                return True
            
            if (i, sumSoFar) in dp:
                return dp[(i, sumSoFar)]
            
            dp[(i, sumSoFar)] = backTrack(i + 1, sumSoFar + nums[i]) or backTrack(i + 1, sumSoFar)

            return dp[(i, sumSoFar)]
                    
        return backTrack(0, 0)