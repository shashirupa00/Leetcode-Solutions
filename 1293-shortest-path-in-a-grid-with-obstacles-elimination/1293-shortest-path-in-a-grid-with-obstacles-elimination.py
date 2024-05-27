class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        
        minHeap = [(0, 0, 0, 0)]
        heapq.heapify(minHeap)
        visited = set((0,0,0))
        rows, cols = len(grid), len(grid[0])

        while minHeap:
            
            dist, x, y, r = heapq.heappop(minHeap)

            if (x, y) == (rows-1, cols-1): return dist

            for dx, dy in [[0,1], [1,0], [-1,0], [0,-1]]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols:
                    if grid[nx][ny] == 1 and r+1 <= k and (nx, ny, r + 1) not in visited:
                        visited.add((nx, ny, r+1))
                        heapq.heappush(minHeap, (dist+1, nx, ny, r+1))
                    elif grid[nx][ny] == 0 and (nx, ny, r) not in visited:
                        visited.add((nx, ny, r))
                        heapq.heappush(minHeap, (dist+1, nx, ny, r))
            
        return -1
