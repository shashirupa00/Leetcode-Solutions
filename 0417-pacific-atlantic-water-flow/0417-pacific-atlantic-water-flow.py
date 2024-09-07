class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        rows, cols = len(heights), len(heights[0])
        pacificSet = set()
        atlanticSet = set()

        def dfs(i, j, visited, prev):
            
            if not (0 <= i < rows) or not (0 <= j < cols) or (i, j) in visited or heights[i][j] < prev:
                return
            
            visited.add((i, j))
            
            dfs(i + 1, j, visited, heights[i][j])
            dfs(i, j + 1, visited, heights[i][j])
            dfs(i - 1, j, visited, heights[i][j])
            dfs(i, j - 1, visited, heights[i][j])
            
            return
        
        for j in range(0, cols):
            dfs(0, j, pacificSet, heights[0][j])
            dfs(rows - 1, j, atlanticSet, heights[rows-1][j])
        
        for i in range(0, rows):
            dfs(i, 0, pacificSet, heights[i][0])
            dfs(i, cols - 1, atlanticSet, heights[i][cols-1])
        
        return list(pacificSet.intersection(atlanticSet))