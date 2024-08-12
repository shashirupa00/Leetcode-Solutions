class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        
        
        def numberOfIslands(grid):

            rows, cols = len(grid), len(grid[0])
            visited = set()
            res = 0

            def dfs(i, j):
                
                if i not in range(rows) or j not in range(cols) or (i, j) in visited or grid[i][j] == 0:
                    return
                
                visited.add((i, j))

                dfs(i + 1, j)
                dfs(i, j + 1)
                dfs(i - 1, j)
                dfs(i, j - 1)

                return
            
            for i in range(rows):
                for j in range(cols):
                    if grid[i][j] == 1 and (i, j) not in visited:
                        dfs(i, j)
                        res += 1

            return res
        
        if numberOfIslands(grid) >= 2 or numberOfIslands(grid) == 0: return 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    if numberOfIslands(grid) >= 2 or numberOfIslands(grid) == 0:
                        return 1
                    grid[i][j] = 1

        return 2