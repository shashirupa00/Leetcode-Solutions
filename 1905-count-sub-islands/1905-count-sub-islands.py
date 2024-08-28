class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        
        rows, cols = len(grid1), len(grid2[0])
        res = 0
        visited = set()
        temp = True

        def dfs(i, j):

            nonlocal temp
            
            if i not in range(rows) or j not in range(cols) or grid2[i][j] == 0 or (i, j) in visited:
                return
            
            if grid2[i][j] != grid1[i][j]:
                temp = False
            
            visited.add((i, j))

            dfs(i + 1, j)
            dfs(i, j + 1)
            dfs(i - 1, j)
            dfs(i, j - 1)

            return
        
        for i in range(rows):
            for j in range(cols):
                temp = True
                if grid2[i][j] == 1 and (i, j) not in visited:
                    dfs(i, j)
                    if temp:
                        res += 1
        
        return res
