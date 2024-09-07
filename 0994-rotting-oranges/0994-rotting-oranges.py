class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        rows, cols = len(grid), len(grid[0])
        totalOranges, rottenOranges = 0, 0
        visited = set()
        deq = collections.deque([])
        res = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    deq.append((i, j))
                    rottenOranges += 1
                    totalOranges += 1
                elif grid[i][j] == 1:
                    totalOranges += 1
        
        while deq:
            for _ in range(len(deq)):
                
                i, j = deq.popleft()

                for dx, dy in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
                    x, y = i + dx, j + dy
                    if x not in range(rows) or y not in range(cols) or (x, y) in visited or grid[x][y] != 1:
                        continue
                    rottenOranges += 1
                    deq.append((x, y))
                    visited.add((x, y))
            res += 1
        
        return res - 1 if totalOranges == rottenOranges else -1