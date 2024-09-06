class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        
        rows, cols = len(matrix), len(matrix[0])
        newMatrix = [[1 if matrix[i][j] == "1" else 0 for j in range(cols)] for i in range(rows)]

        for i in range(1, rows):
            for j in range(cols):
                if newMatrix[i][j]:
                    newMatrix[i][j] += newMatrix[i-1][j]
             
        res = 0

        for i in range(rows):

            stack = []
            
            for j in range(cols):
                
                start = j

                while stack and stack[-1][0] >= newMatrix[i][j]:

                    num, idx = stack.pop()
                    res = max(res, num * (j - idx))
                    start = idx
                
                stack.append([newMatrix[i][j], start])
            
            while stack:
                num, idx = stack.pop()
                res = max(res, num * (cols - idx))
        
        return res
