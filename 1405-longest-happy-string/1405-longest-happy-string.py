class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        
        minHeap = []
        
        if a != 0:
            minHeap.append((-a, 'a'))
        
        if b != 0:
            minHeap.append((-b, 'b'))
        
        if c != 0:
            minHeap.append((-c, 'c'))
            
        heapq.heapify(minHeap)
        res = ""
        curCount = 0

        while minHeap:
            
            temp = None

            if res and res[-1] == minHeap[0][1] and curCount == 2:
                
                temp = heapq.heappop(minHeap)
                if not minHeap:
                    return res
            
            count, char = heapq.heappop(minHeap)
            
            if res and char == res[-1]:
                curCount += 1
            
            else:
                curCount = 1

            if count < 0: res += char

            if count + 1 < 0:
                heapq.heappush(minHeap, (count + 1, char))
            
            if temp:
                heapq.heappush(minHeap, temp)
        
        return res