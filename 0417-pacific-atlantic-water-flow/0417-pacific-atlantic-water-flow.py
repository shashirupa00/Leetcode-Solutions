class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        if not heights:
            return []

        rows, cols = len(heights), len(heights[0])
        pSet, aSet = set(), set()

        def dfs(i, j, oceanSet, prevNode):
            
            if i not in range(rows) or j not in range(cols) or (i, j) in oceanSet or heights[i][j] < prevNode:
                return
            
            oceanSet.add((i, j))

            dfs(i + 1, j, oceanSet, heights[i][j])
            dfs(i, j + 1, oceanSet, heights[i][j])
            dfs(i - 1, j, oceanSet, heights[i][j])
            dfs(i, j - 1, oceanSet, heights[i][j])

            return
        
        for j in range(cols):
            dfs(0, j, pSet, float("-inf"))
            dfs(rows - 1, j, aSet, float("-inf"))
        
        for i in range(rows):
            dfs(i, 0, pSet, float("-inf"))
            dfs(i, cols - 1, aSet, float("-inf"))

        res = []

        for pair in aSet:
            if pair in pSet:
                res.append(list(pair))
        
        return res