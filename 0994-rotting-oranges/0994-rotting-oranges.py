class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        deq = collections.deque([])
        directions = [[0,1],[1,0],[-1,0],[0,-1]]
        fresh, minutes = 0, -1

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    deq.append((i,j))
                elif grid[i][j] == 1:
                    fresh += 1
        
        if not deq and not fresh: return 0
                
        while deq:
            for i in range(len(deq)):
                r, c = deq.popleft()
                for x,y in directions:
                    a, b = r+x, c+y

                    if (a in range(rows) and
                    b in range(cols) and
                    grid[a][b] == 1):
                        grid[a][b] = 2
                        deq.append((a,b))

            minutes += 1
                                       
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    return -1
        
        return minutes
