class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:

        rows, cols = len(grid), len(grid[0])
        visited = set()
        res = 0
        
        def backTrack(i, j, curSum):
            
            if i not in range(rows) or j not in range(cols) or (i, j) in visited or grid[i][j] == 0:
                return curSum
            
            visited.add((i, j))

            curSum += grid[i][j] + max(backTrack(i + 1, j, curSum), backTrack(i, j + 1, curSum), backTrack(i - 1, j, curSum),
                                    backTrack(i, j - 1, curSum))
            
            visited.remove((i, j))

            return curSum
        
        for i in range(rows):
            for j in range(cols):
                visited = set()
                if grid[i][j] != 0: res = max(res, backTrack(i, j, 0))
        
        return res