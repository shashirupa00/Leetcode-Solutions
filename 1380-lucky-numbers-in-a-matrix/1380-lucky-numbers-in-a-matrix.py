class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        
        rows, cols = len(matrix), len(matrix[0])
        res = []

        for i in range(rows):
            minEl = min(matrix[i])
            for j in range(cols):
                maxEl = max([matrix[r][j] for r in range(rows)])
                if matrix[i][j] == minEl == maxEl:
                    res.append(matrix[i][j])
        
        return res