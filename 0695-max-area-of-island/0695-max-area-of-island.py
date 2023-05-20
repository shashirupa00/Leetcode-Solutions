class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        deq = collections.deque([])
        rows, cols = len(grid), len(grid[0])
        visited = set()
        maxArea = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    area = 0
                    deq.append((i,j))
                    visited.add((i,j))
                    while deq:
                        x, y = deq.popleft()
                        area += 1

                        directions = [[0,1],[1,0],[0,-1],[-1,0]]

                        for k in range(len(directions)):
                            r, c = x+directions[k][0], y+directions[k][1]
                             
                            if (0 <= r <= rows-1 and
                            0 <= c <= cols-1 and
                            grid[r][c] == 1 and
                            (r,c) not in visited):

                                deq.append((r,c))
                                visited.add((r,c))
                    
                    maxArea = max(maxArea, area)
        
        return maxArea