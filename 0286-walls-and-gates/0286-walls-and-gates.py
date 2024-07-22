class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        
        rows, cols = len(rooms), len(rooms[0])
        deq = collections.deque([])
        visited = set()

        for i in range(rows):
            for j in range(cols):
                if rooms[i][j] == 0:
                    deq.append((i, j, 0))
                    visited.add((i, j))
        
        while deq:
            for _ in range(len(deq)):

                x, y, dist = deq.popleft()

                for dx, dy in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                    nx, ny = x + dx, y + dy
                    if (0 <= nx < rows and 0 <= ny < cols and  
                    (nx, ny) not in visited and rooms[nx][ny] != -1):
                        rooms[nx][ny] = dist + 1
                        deq.append((nx, ny, dist + 1))
                        visited.add((nx, ny))
        
