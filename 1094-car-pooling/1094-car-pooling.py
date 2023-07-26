class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:

        curCapacity = 0
        trips.sort(key = lambda x:x[1])
        minHeap = []
        heapq.heapify(minHeap)

        for trip in trips:

            while minHeap and trip[1] >= minHeap[0][0]:
                endTime, cap = heapq.heappop(minHeap)
                curCapacity -= cap

            curCapacity += trip[0]
            
            if curCapacity > capacity:
                return False     
  
            heapq.heappush(minHeap, (trip[2], trip[0]))

        return True


        

        