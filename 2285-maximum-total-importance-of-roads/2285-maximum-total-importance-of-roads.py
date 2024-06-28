class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        
        hashMap = defaultdict(int)

        for u, v in roads:
            hashMap[u] += 1
            hashMap[v] += 1
        
        minHeap = []
        res = 0

        for i in range(n):
            minHeap.append(-hashMap[i])
        
        heapq.heapify(minHeap)

        while n >= 1:

            res += n * -1 * heapq.heappop(minHeap)
            n -= 1
        
        return res