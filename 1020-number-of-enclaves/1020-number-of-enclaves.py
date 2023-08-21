class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:

        rows, cols = len(grid), len(grid[0])
        border, count = 0, 0
        res = 0
        visited = set()

        def dfs(r, c):

            nonlocal border
            nonlocal count

            if (r not in range(rows) or 
                (c not in range(cols)) or
                ((r, c) in visited) or
                (grid[r][c] != 1)):

                return 0
            
            visited.add((r, c))
            count += 1

            if r == 0 or c == 0 or r == rows - 1 or c == cols-1:
                border = 1
            
            dfs(r+1, c)
            dfs(r, c+1)
            dfs(r-1, c)
            dfs(r, c-1)

            return count
        
        for r in range(rows):
            for c in range(cols):
                if (r, c) not in visited and grid[r][c] == 1:
                    dfs(r, c)
                    if not border: res += count
                    border = 0
                    count = 0
        
        return res