class Solution:
    def maxArea(self, height: List[int]) -> int:

        i, j = 0 , len(height)-1
        maxSoFar = float("-inf")

        while i<j:
            area = min(height[i], height[j]) * (j-i)
            maxSoFar = max(maxSoFar, area)

            if height[i] > height[j]:
                j -= 1
            
            else:
                i += 1
        
        return int(maxSoFar)

        