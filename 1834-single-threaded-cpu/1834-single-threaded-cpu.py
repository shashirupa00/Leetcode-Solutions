class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        
        tasks = [[a, b, i] for i, (a, b) in enumerate(tasks)]
        tasks = sorted(tasks, key= lambda x: (x[0], x[1]))
        minHeap = [(tasks[0][1], tasks[0][2])]
        i = 1
        heapq.heapify(minHeap)
        curTime = tasks[0][0]
        res = []

        while minHeap:
            
            time, task = heapq.heappop(minHeap)
            curTime += time

            res.append(task)

            while i < len(tasks) and tasks[i][0] <= curTime:
                heapq.heappush(minHeap, (tasks[i][1], tasks[i][2]))
                i += 1
            
            if i < len(tasks) and not minHeap:
                heapq.heappush(minHeap, (tasks[i][1], tasks[i][2]))
                curTime = tasks[i][0]
                i += 1
        
        return res
