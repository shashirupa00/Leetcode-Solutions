class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        
        res = 0
        arr = [r1 - r2 for r1, r2 in zip(reward1, reward2)]
        minHeap1 = [(-r, i) for i, r in enumerate(arr)]
        minHeap2 = [(-r, i) for i, r in enumerate(reward2)]

        p = len(reward1) - k
        visited = set()

        heapq.heapify(minHeap1)
        heapq.heapify(minHeap2)

        while k:
            r, i = heapq.heappop(minHeap1)

            res += reward1[i]
            k -= 1
            visited.add(i)
        
        while p:

            r, i = heapq.heappop(minHeap2)

            if i not in visited:
                res += -1 * r
                p -= 1
        
        return res
        
        return res
