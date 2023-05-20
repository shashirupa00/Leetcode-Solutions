class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        rows, cols = len(heights), len(heights[0])
        atl = set()
        pac = set()
        # directions = [[0,1], [1,0], [0,-1], [-1,0]]
        res = []


        def dfs(i, j, reach, prev):
            if (i < 0 or 
            i >= rows or
            j < 0 or
            j >= cols or
            (i,j) in reach or
            heights[i][j] < prev):
                    return

            reach.add((i,j))
            
            dfs(i+1, j, reach, heights[i][j])
            dfs(i-1, j, reach, heights[i][j])
            dfs(i, j+1, reach, heights[i][j])
            dfs(i, j-1, reach, heights[i][j])
        
        for c in range(cols):
            dfs(0, c, pac, heights[0][c])
            dfs(rows - 1, c, atl, heights[rows - 1][c])

        for r in range(rows):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, cols - 1, atl, heights[r][cols - 1])
        
        for i in range(rows):
            for j in range(cols):
                if (i,j) in atl and (i,j) in pac:
                    res.append([i,j])

        return res




        