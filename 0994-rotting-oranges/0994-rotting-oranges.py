class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        rows, cols = len(grid), len(grid[0])
        oranges, rotten = 0, 0
        deq = collections.deque([])
        visited = set()
        minutes = -1

        for i in range(rows):
            for j in range(cols):
                if grid[i][j]:
                    oranges += 1
                if grid[i][j] == 2:
                    deq.append((i, j))
                    visited.add((i, j))

        while deq:
            for _ in range(len(deq)):
                
                x, y = deq.popleft()
                rotten += 1

                for dx, dy in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
                    nx, ny = x + dx, y + dy
                    if (0 <= nx < rows and 0 <= ny < cols and  
                    (nx, ny) not in visited and grid[nx][ny] == 1):
                        deq.append((nx, ny))
                        visited.add((nx, ny))

            minutes += 1
        
        return minutes if rotten == oranges else -1
        
