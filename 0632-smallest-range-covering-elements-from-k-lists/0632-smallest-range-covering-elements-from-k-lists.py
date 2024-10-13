class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        
        minHeap = [(nums[l][0], l, 0) for l in range(len(nums))]
        minRange = float("inf")
        heapq.heapify(minHeap)
        maxNum = max([i[0] for i in nums])
        res = [0, 0]

        while True:

            if minRange > maxNum - minHeap[0][0]:
                minRange = maxNum - minHeap[0][0]
                res = [minHeap[0][0], maxNum]

            _, listIdx, idx = heapq.heappop(minHeap)

            if idx + 1 >= len(nums[listIdx]):
                break

            heapq.heappush(minHeap, (nums[listIdx][idx + 1], listIdx, idx + 1))
            maxNum = max(maxNum, nums[listIdx][idx + 1])

        return res 