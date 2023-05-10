class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        deq = collections.deque()
        hashMap = {}
        time = 0
        
        for task in tasks:
            hashMap[task] = 1 + hashMap.get(task ,0)
        
        freq = sorted(hashMap.values())

        freq = [-num for num in freq]

        heapq.heapify(freq)

        while freq or deq:

            if freq:
                curr = heapq.heappop(freq)
                if curr+1 != 0:
                    deq.append((curr+1, time+n+1))
            
            time += 1

            if deq and time == deq[0][1]:
                heapq.heappush(freq, deq.popleft()[0])

        return time
            




