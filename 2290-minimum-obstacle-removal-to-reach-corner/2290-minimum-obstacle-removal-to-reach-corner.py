class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        deque_ = deque([(0, 0, 0)]) 
        visited = set((0, 0))

        while deque_:
            obs, i, j = deque_.popleft()
            
            if (i, j) == (rows - 1, cols - 1):
                return obs

            for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
                ni, nj = i + di, j + dj
                
                if 0 <= ni < rows and 0 <= nj < cols and (ni, nj) not in visited:
                    visited.add((ni, nj))
                    if grid[ni][nj] == 1:
                        deque_.append((obs + 1, ni, nj))
                    else:
                        deque_.appendleft((obs, ni, nj))
        

