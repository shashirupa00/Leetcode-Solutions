class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        hashSet, minHeap = {0}, []
        heapq.heapify(minHeap)
        cost = point = 0

        while len(hashSet) < len(points):
            i = point
            for j in range(len(points)):

                if j in hashSet: continue

                mDist = abs(points[i][0]-points[j][0]) + abs(points[i][1]- points[j][1])
                heapq.heappush(minHeap, (mDist, j))
            
            while point in hashSet:
                d, point = heapq.heappop(minHeap)

            cost += d
            hashSet.add(point)
        
        return cost











            
        

