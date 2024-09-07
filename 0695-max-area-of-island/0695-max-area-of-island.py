class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        rows, cols = len(grid), len(grid[0])
        visited = set()
        res, area = 0, 0

        def dfs(i, j):
            
            nonlocal area

            if i not in range(rows) or j not in range(cols) or (i, j) in visited or not grid[i][j]:
                return
            
            area += 1
            visited.add((i, j))

            dfs(i + 1, j)
            dfs(i, j + 1)
            dfs(i - 1, j)
            dfs(i, j - 1)

            return
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] and (i, j) not in visited:
                    area = 0
                    dfs(i, j)
                    res = max(res, area)
        
        return res