class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        
        maxHeap = [-num for num in nums]
        heapq.heapify(maxHeap)
        res = 0

        while k:

            curNum = -1 * (heapq.heappop(maxHeap))
            res += curNum

            heapq.heappush(maxHeap, -1 * math.ceil(curNum / 3))
            k -= 1
        
        return res