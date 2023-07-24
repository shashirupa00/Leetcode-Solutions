class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        if grid[0][0] != 0: return -1
        
        rows, cols = len(grid), len(grid[0])
        deq = collections.deque([(0, 0)])
        visited = set()
        res = 1
        directions = [[0,1],[1,0],[-1,0],[0,-1],[-1,-1],[-1,1],[1,-1],[1,1]]

        while deq:
            for _ in range(len(deq)):

                r, c = deq.popleft()
                visited.add((r, c))

                if (r, c) == (rows-1, cols-1): return res

                for x, y in directions:

                    i, j = r+x, c+y

                    if((i not in range(rows)) or (j not in range(cols)) or ((i,j) in visited) or (grid[i][j] != 0)):
                        continue

                    deq.append((i, j))
                    visited.add((i, j))

            res += 1
        
        return -1
