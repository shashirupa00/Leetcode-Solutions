class Solution:
    def timeTaken(self, arrival: List[int], state: List[int]) -> List[int]:
        
        enterQueue = collections.deque([])
        exitQueue = collections.deque([])
        prev = None
        i = 0
        curTime = arrival[0]
        res = [0 for _ in arrival]

        while curTime <= arrival[-1] or enterQueue or exitQueue:

            while i < len(arrival) and arrival[i] == curTime:
                if state[i]:
                    exitQueue.append(i)
                else:
                    enterQueue.append(i)
                i += 1
            
            if prev and enterQueue and exitQueue:

                if prev[0] == "enter" and prev[1] == curTime - 1:
                    person = enterQueue.popleft()
                    res[person] = curTime
                    prev = ["enter", curTime]
                
                else:
                    person = exitQueue.popleft()
                    res[person] = curTime
                    prev = ["exit", curTime]
            
            else:
                if exitQueue:
                    person = exitQueue.popleft()
                    res[person] = curTime
                    prev = ["exit", curTime]
                
                elif enterQueue:
                    person = enterQueue.popleft()
                    res[person] = curTime
                    prev = ["enter", curTime]
            
            curTime += 1

        return res


            
            