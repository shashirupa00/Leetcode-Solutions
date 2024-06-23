class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        
        deq = collections.deque(sorted(nums))
        avgs = []

        while deq:
            minEl, maxEl = deq.popleft(), deq.pop()
            avgs.append((minEl + maxEl) / 2)
        
        return min(avgs)