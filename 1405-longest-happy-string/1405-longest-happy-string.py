class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
       
        hashMap = {'a': a, 'b': b, 'c': c}
        minHeap = []

        for key, value in hashMap.items():
            if value:
                minHeap.append((-1*value, key))

        heapq.heapify(minHeap)
        prevCount = 0
        res = ""

        while minHeap:
            
            count, char = heapq.heappop(minHeap)
            count *= -1

            if len(res) > 1 and res[-1] == res[-2] == char:

                if not minHeap:
                    break

                newCount, newChar = heapq.heappop(minHeap)
                newCount *= -1
                
                res += newChar
                newCount -= 1

                if newCount > 0:
                    heapq.heappush(minHeap, (-1*newCount, newChar))
                
                heapq.heappush(minHeap, (-1*count, char))
                
            else:                
                res += char
                count -= 1

                if count > 0:
                    heapq.heappush(minHeap, (-1*count, char))

        return res