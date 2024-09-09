class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        rows, cols = len(matrix), len(matrix[0])
        dp = defaultdict(int)
        res = 0

        def dfs(i, j, prev):
            
            if i not in range(rows) or j not in range(cols) or prev >= matrix[i][j]:
                return 0
            
            if (i, j) in dp:
                return dp[(i, j)]
            
            dp[(i, j)] = 1 + max(dfs(i + 1, j, matrix[i][j]), dfs(i , j + 1, matrix[i][j]), 
                                    dfs(i - 1, j, matrix[i][j]), dfs(i, j - 1, matrix[i][j]))

            return dp[(i, j)]
        
        for i in range(rows):
            for j in range(cols):
                res = max(res, dfs(i, j, float("-inf")))
        
        return res