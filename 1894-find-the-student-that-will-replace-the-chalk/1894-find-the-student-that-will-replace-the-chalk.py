class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        
        totalSum = sum(chalk)
        i = k // totalSum

        if i * totalSum == k:
            return 0
        
        curSum = totalSum * i

        for i in range(len(chalk)):
            curSum += chalk[i]
            if curSum > k:
                return i
