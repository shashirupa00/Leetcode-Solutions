class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort()
        res = []

        for interval in intervals:

            newInterval = interval

            if res and res[-1][1] >= interval[0]:

                prevInterval = res.pop()
                newInterval = [prevInterval[0], newInterval[1]] 
            
            res.append(newInterval)
        
        return res