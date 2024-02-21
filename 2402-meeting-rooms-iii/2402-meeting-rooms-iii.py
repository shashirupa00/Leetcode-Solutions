class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        
        meetings.sort()
        rooms = [i for i in range(n)]
        hashMap = defaultdict(int)
        minHeap = []
        res, ans = 0, 0

        heapq.heapify(rooms)
        heapq.heapify(minHeap)
        
        for start, end in meetings:

            while minHeap and start >= minHeap[0][0]:
                curEnd, room = heapq.heappop(minHeap)
                heapq.heappush(rooms, room)

            if not rooms:
                curEnd, room = heapq.heappop(minHeap)
                end = end + curEnd - start
                heapq.heappush(rooms, room)

            room = heapq.heappop(rooms)
            heapq.heappush(minHeap, (end, room))
            hashMap[room] += 1

        for key, value in hashMap.items():
            if value > res:
                res = value
                ans = key

        return ans