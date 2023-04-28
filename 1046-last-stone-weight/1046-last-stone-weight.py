class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        stones = [-num for num in stones]
        heapq.heapify(stones)

        while len(stones) >= 2:
            y, x = -1 * heapq.heappop(stones), -1 * heapq.heappop(stones)

            if x != y:
                z = (y-x) * -1
                heapq.heappush(stones, z)
            
        return 0 if not stones else -1*stones[0]





