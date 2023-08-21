class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        
        nums = [-1 * int(num) for num in nums]
        heapq.heapify(nums)

        while k:

            cur = heapq.heappop(nums)
            k -= 1
            if not k: return str(-1 * cur)