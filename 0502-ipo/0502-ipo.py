class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:

        maxP = []
        minCapital = [(i, j) for i, j in zip(capital, profits)]
        heapq.heapify(minCapital)

        for i in range(k):

            while minCapital and minCapital[0][0] <= w:
                c, p = heapq.heappop(minCapital)
                heapq.heappush(maxP, -1 * p)

            if maxP:
                w += -1 * heapq.heappop(maxP)

        return w

        