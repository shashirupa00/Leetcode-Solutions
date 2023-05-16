class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        stack = []
        maxArea, index = 0, 0

        for i in range(len(heights)):

            if stack and heights[i] < stack[-1][1]:

                while stack and heights[i] < stack[-1][1]:
                    index, currHeight = stack.pop()
                    area = currHeight * (i-index)
                    maxArea = max(maxArea, area)
                
                stack.append((index, heights[i]))
            
            else:
                stack.append((i, heights[i]))
        
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))

        return maxArea
