class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        
        rows, cols = len(rooms), len(rooms[0])
        deq = collections.deque([])

        for i in range(rows):
            for j in range(cols):
                if rooms[i][j] == 0:
                    deq.append((i, j, 0))
        
        while deq:
            for _ in range(len(deq)):
                
                r, c, dist = deq.popleft()

                for dr, dc in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
                    nr, nc = r + dr, c + dc
                    if nr not in range(rows) or nc not in range(cols) or rooms[nr][nc] != 2147483647:
                        continue
                    rooms[nr][nc] = dist + 1
                    deq.append((nr, nc, dist + 1))
                    