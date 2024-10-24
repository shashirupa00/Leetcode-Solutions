class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        '''
        empty grid is possible
        even dimensions
        only 1s and 0s but strings
        no diagonal neighbhors 

        input: mxn 2d array with 1s and 0s
        output: integer
        '''

        rows, cols = len(grid), len(grid[0])
        res = 0
        visited = set()

        def dfs(i, j):
            
            if i not in range(rows) or j not in range(cols) or (i, j) in visited or grid[i][j] == '0':
                return
            
            visited.add((i, j))

            dfs(i + 1, j)
            dfs(i, j + 1)
            dfs(i - 1, j)
            dfs(i, j - 1)

            return 
            
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1' and (i, j) not in visited:
                    dfs(i, j)
                    res += 1
        
        return res