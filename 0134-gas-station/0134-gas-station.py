class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        if sum(gas) < sum(cost): return -1
        res = 0
        sumSoFar = 0

        for i in range(len(gas)):
            if sumSoFar < 0:
                res = i
                sumSoFar = 0

            sumSoFar += gas[i] - cost[i]
        
        return res

            

