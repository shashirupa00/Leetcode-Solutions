class Solution:
    def reorganizeString(self, s: str) -> str:
        
        counter = Counter(s)
        minHeap = [(-counter[key], key) for key in counter]
        heapq.heapify(minHeap)
        res = ""

        while minHeap:

            temp = None

            if res and minHeap[0][1] == res[-1]:
                temp = heapq.heappop(minHeap)
                
                if not minHeap:
                    return ""

            count, char = heapq.heappop(minHeap)
            res += char

            if count + 1 != 0:
                heapq.heappush(minHeap, (count + 1, char))
            
            if temp:
                heapq.heappush(minHeap, temp)
        
        return res