class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        
        rows, cols = len(grid), len(grid[0])
        visited = set()
        allIslands = []
        uniqueIslands = set()
        curIsland = []

        def dfs(i, j):
            
            if not (0 <= i < rows) or not (0 <= j < cols) or (i, j) in visited or grid[i][j] == 0:
                return
            
            visited.add((i, j))
            curIsland.append([i, j])

            dfs(i + 1, j)
            dfs(i, j + 1)
            dfs(i - 1, j)
            dfs(i, j - 1)

            return
        
        def translate(island):
            
            offsetX, offsetY = island[0][0], island[0][1]
            newIsland = []

            for x, y in island:
                newIsland.append((x - offsetX, y - offsetY))
            
            uniqueIslands.add(tuple(newIsland))

        
        for i in range(rows):
            for j in range(cols):
                curIsland = []
                if grid[i][j] and (i, j) not in visited:
                    dfs(i, j)
                    allIslands.append(tuple(curIsland))
        
        for island in allIslands:
            translate(island)
        
        return len(uniqueIslands)
                    