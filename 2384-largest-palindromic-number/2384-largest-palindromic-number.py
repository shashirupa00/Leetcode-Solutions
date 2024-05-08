class Solution:
    def largestPalindromic(self, num: str) -> str:
        
        counter = Counter(num)
        maxHeap = [(-int(key), val) for key, val in counter.items()]
        first, second = "", ""
        maxOdd = -1
        heapq.heapify(maxHeap)

        while maxHeap:

            num, freq = heapq.heappop(maxHeap)
            num = num * -1
            temp = freq // 2

            if temp:
                first = first + (str(num) * temp)
                second = (str(num) * temp) + second
            
            if freq % 2:
                maxOdd = max(maxOdd, num)
        
        print(first, maxOdd, second)
        res = first + (str(maxOdd) if maxOdd != -1 else "") + second
        i, j = 0, len(res) - 1

        while i < len(res) and res[i] == '0':
            i += 1
        
        while j >= 0 and res[j] == "0":
            j -= 1

        return res[i:j+1] if res[i:j+1] else "0"