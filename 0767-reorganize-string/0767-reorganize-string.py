class Solution:
    def reorganizeString(self, s: str) -> str:   

        counter = Counter(s)
        minHeap = [(-1 * val, key) for key, val in counter.items()]
        heapq.heapify(minHeap)
        res = ""

        while minHeap:

            count, char = heapq.heappop(minHeap)
            count = count * -1

            if res and char == res[-1]:
                
                if not minHeap:
                    return ""

                newCount, newChar = heapq.heappop(minHeap)
                newCount = newCount * -1

                res += newChar
                
                if newCount - 1:
                    heapq.heappush(minHeap, ((newCount - 1) * -1, newChar))
                
                heapq.heappush(minHeap, (count * -1, char))
            
            else:
                res += char

                if count - 1:
                    heapq.heappush(minHeap, ((count - 1) * -1, char))
        
        return res