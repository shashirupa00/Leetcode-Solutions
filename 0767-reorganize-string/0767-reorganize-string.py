class Solution:
    def reorganizeString(self, s: str) -> str:
        
        res = ""
        hashMap = collections.Counter(s)
        minHeap = [(-1*val, key) for key, val in hashMap.items()]
        heapq.heapify(minHeap)

        while minHeap:

            count, char = heapq.heappop(minHeap)
            count *= -1

            if res and res[-1] == char:

                if not minHeap:
                    return ""
                
                newCount, newChar = heapq.heappop(minHeap)
                newCount *= -1

                res += newChar
                newCount -= 1

                if newCount:
                    heapq.heappush(minHeap, (newCount*-1, newChar))
                
                heapq.heappush(minHeap, (count*-1, char))
                
            
            else:
                res += char
                count -= 1

                if count:
                    heapq.heappush(minHeap, (count*-1, char))
        
        return res

