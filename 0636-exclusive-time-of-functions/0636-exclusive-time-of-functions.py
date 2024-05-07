class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:

        res = [0 for i in range(n)]
        stack = []

        for i in range(len(logs)):

            logID, logType, logTime = logs[i].split(":")

            if logType == "start":

                if stack:
                    curID, curTime = stack[-1]
                    res[curID] += int(logTime) - curTime

                stack.append([int(logID), int(logTime)])

            elif logType == "end":

                curID, curTime = stack.pop()
                res[curID] += int(logTime) - curTime + 1
                
                if stack:
                    stack[-1][-1] = int(logTime) + 1
        
        return res

