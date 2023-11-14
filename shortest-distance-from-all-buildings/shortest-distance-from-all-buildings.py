class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:

        rows, cols = len(grid), len(grid[0])
        res = float("inf")
        empty = set([(i, j) for i in range(rows) for j in range(cols) if grid[i][j] == 0])
        buildings = set([(i, j) for i in range(rows) for j in range(cols) if grid[i][j] == 1])
        hashMap = collections.defaultdict(int)
        distanceGrid = [[0] * cols for _ in range(rows)]


        def bfs(i, j):
            
            deq = collections.deque([(i, j, 0)])
            visited = set()

            while deq:
                for _ in range(len(deq)):

                    r, c, dist = deq.popleft()

                    for dx, dy in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
                        x, y = r + dx, c + dy

                        if x < 0 or x >= rows or y < 0 or y >= cols or (x, y) not in empty or (x, y) in visited:
                            continue

                        distanceGrid[x][y] += dist + 1
                        hashMap[(x, y)] += 1
                        deq.append((x, y, dist + 1))
                        visited.add((x, y))
            
        for i, j in buildings:
            bfs(i, j)
        
        for i, j in empty:
            if hashMap[(i, j)] == len(buildings):
                res = min(res, distanceGrid[i][j] )
    
        return res if res != float("inf") else -1