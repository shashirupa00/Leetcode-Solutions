class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        visited = set()
        islands = 0
        rows, cols = len(grid), len(grid[0])
        deq = collections.deque([])

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i,j) not in visited: 
                    deq.append((i,j))
                    while deq:
                        x, y = deq.popleft()

                        directions = [[1,0],[0,1],[-1,0],[0,-1]]
                        
                        for k in range(len(directions)):
                            r, c = x+directions[k][0], y+directions[k][1]

                            if (
                                0<=r<=rows-1
                                and 0<=c<=cols-1
                                and grid[r][c] == "1"
                                and (r, c) not in visited
                            ):

                                deq.append((r,c))
                                visited.add((r,c))

                    islands += 1
    
        return islands

            
