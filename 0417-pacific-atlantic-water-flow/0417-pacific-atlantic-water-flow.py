class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        rows, cols = len(heights), len(heights[0])
        pSet = set()
        aSet = set()
        res = []

        def dfs(i, j, prev, ocean, visited):

            if i not in range(rows) or j not in range(cols) or (i, j) in visited or heights[i][j] < prev:
                return
            
            ocean.add((i, j))
            visited.add((i, j))

            dfs(i+1, j, heights[i][j], ocean, visited)
            dfs(i, j+1, heights[i][j], ocean, visited)
            dfs(i-1, j, heights[i][j], ocean, visited)
            dfs(i, j-1, heights[i][j], ocean, visited)

            return
        
        for i in range(cols):
            dfs(rows-1, i, float("-inf"), aSet, set())
            dfs(0, i, float("-inf"), pSet, set())
        
        for i in range(rows):
            dfs(i, cols-1, float("-inf"), aSet, set())
            dfs(i, 0, float("-inf"), pSet, set())
        
        for subList in aSet:
            if subList in pSet:
                res.append(list(subList))
        
        return res
        