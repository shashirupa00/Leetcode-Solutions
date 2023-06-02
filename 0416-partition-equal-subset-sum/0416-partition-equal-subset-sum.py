class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        totalSum = sum(nums)

        if totalSum%2 == 1: return False

        target = totalSum//2
        sums = [0, nums[-1]]
        visited = set(sums)

        for i in range(len(nums)-2, -1, -1):
            for j in range(len(sums)):
                currSum = nums[i] + sums[j]

                if currSum == target: return True

                if currSum < target and currSum not in visited:
                    sums.append(currSum)
                    visited.add(currSum)
        
        return False


                




