class Solution:
    def nthUglyNumber(self, n: int) -> int:

        if n == 1:
            return 1
        
        minHeap = [1]
        heapq.heapify(minHeap)
        visited = set([1])

        for i in range(n):

            cur = heapq.heappop(minHeap)

            for num in [2, 3, 5]:
                if cur * num not in visited:
                    heapq.heappush(minHeap, cur * num)
                    visited.add(cur * num)
        
        return cur