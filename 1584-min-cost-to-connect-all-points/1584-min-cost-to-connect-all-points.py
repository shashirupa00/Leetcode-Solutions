class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        minHeap = []
        heapq.heapify(minHeap)
        res = 0
        
        if len(points) <= 1:
            return 0

        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                p1, p2 = points[i], points[j]
                heapq.heappush(minHeap, (abs(p1[0] - p2[0]) + abs(p1[1] - p2[1]), i, j))
        
        visited = set()
        edges = 0

        print(minHeap)

        while edges + 1 != len(points) or len(visited) < len(points):

            dist, i, j = heapq.heappop(minHeap)

            if i not in visited or j not in visited or len(visited) == len(points):
                res += dist
                visited.add(i)
                visited.add(j)
                edges += 1
                print(i, j, edges)

        return res