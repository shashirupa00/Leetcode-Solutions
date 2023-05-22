class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """

        deq = collections.deque([])
        rows, cols = len(rooms),len(rooms[0])
        directions =[[0,1],[1,0],[-1,0],[0,-1]]
        visited = set()
        INF = 2147483647

        for i in range(rows):
            for j in range(cols):
                if rooms[i][j] == 0:
                    deq.append((i,j))
                    visited.add((i,j))

        while deq:
            for _ in range(len(deq)):
                a, b = deq.popleft()

                for x, y in directions:
                    r, c = a+x, b+y

                    if (r not in range(rows) or
                    c not in range(cols) or
                    (r,c) in visited or
                    rooms[r][c] != INF):

                        continue
                    
                    rooms[r][c] = rooms[a][b] + 1
                    deq.append((r,c))
                    visited.add((r,c))
