class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        
        chefStart = 0
        res = 0

        for arrival, time in customers:

            if chefStart < arrival:
                chefStart = arrival
            
            res += (chefStart + time) - arrival
            chefStart += time
        
        return res / len(customers)