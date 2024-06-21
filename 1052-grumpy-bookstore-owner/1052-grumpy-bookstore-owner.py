class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        
        window = collections.deque([])
        loss = 0
        maxLoss, maxWindow = 0, (-1, -1)
        res = 0

        for i in range(len(customers)):

            num, grmp = customers[i], grumpy[i]

            if len(window) >= minutes:

                curNum, curGrmp, idx = window.popleft()

                if curGrmp:
                    loss -= curNum

            if grmp:
                loss += num
        
            window.append((num, grmp, i))

            if maxLoss < loss:
                maxLoss = loss
                maxWindow = window[0][-1], window[-1][-1]
        
        for i, num in enumerate(customers):

            if i < maxWindow[0] or i > maxWindow[1]:
                res += num if not grumpy[i] else 0
        
        if maxWindow != (-1, -1):
            for i in range(maxWindow[0], maxWindow[1]+1):
                res += customers[i]
        
        return res
