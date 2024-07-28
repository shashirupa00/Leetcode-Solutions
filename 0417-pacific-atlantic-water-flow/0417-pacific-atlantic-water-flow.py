class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        rows, cols = len(heights), len(heights[0])
        pacificSet = set()
        atlanticSet = set()

        def dfs(i, j, ocean, visited, prev):
            
            if not (0 <= i < rows) or not (0 <= j < cols) or (i, j) in visited or heights[i][j] < prev:
                return

            ocean.add((i, j))
            visited.add((i, j))
            
            dfs(i + 1, j, ocean, visited, heights[i][j])
            dfs(i, j + 1, ocean, visited, heights[i][j])
            dfs(i - 1, j, ocean, visited, heights[i][j])
            dfs(i, j - 1, ocean, visited, heights[i][j])
            
            return
        
        for j in range(0, cols):
            dfs(0, j, pacificSet, set(), -1)
            dfs(rows - 1, j, atlanticSet, set(), -1)
        
        for i in range(0, rows):
            dfs(i, 0, pacificSet, set(), -1)
            dfs(i, cols - 1, atlanticSet, set(), -1)
        
        return list(pacificSet.intersection(atlanticSet))