class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        
        arr = []
        prefix = 0
        res = float("inf")

        for i, num in enumerate(nums):
            prefix += num
            arr.append((prefix, i))
        
        deq = collections.deque([])

        for num, i in arr:

            while deq and deq[-1][0] <= num:
                deq.pop()
            
            deq.append((num, i))
            if num >= k: res = min(res, i + 1)

            while deq and num - deq[0][0] >= k:
                _, idx = deq.popleft()
                res = min(res, i - idx + 1)

        return res if res != float("inf") else -1