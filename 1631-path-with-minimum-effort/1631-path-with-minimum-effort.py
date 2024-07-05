class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:

        rows, cols = len(heights), len(heights[0])
        minPath = [[float("inf") for i in range(cols)] for j in range(rows)]
        minHeap = [(0, 0, 0)]
        visited = set()

        minPath[0][0] = 0

        heapq.heapify(minHeap)

        while minHeap:

            cur, i, j = heapq.heappop(minHeap)

            visited.add((i, j))

            for dr, dc in [[0, 1], [1, 0], [-1, 0], [0, -1]]:

                r, c = i + dr, j + dc

                if (0 <= r < rows) and (0 <= c < cols) and (r, c) not in visited:

                    diff = abs(heights[i][j] - heights[r][c])
                    maxDiff = max(diff, minPath[i][j])
                    if minPath[r][c] > maxDiff:
                        minPath[r][c] = maxDiff
                        heapq.heappush(minHeap, (maxDiff, r, c))
    
        return minPath[rows-1][cols-1]