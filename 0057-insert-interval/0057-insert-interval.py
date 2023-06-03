class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        res = []

        if not intervals:
            res.append(newInterval)
            return res

        if newInterval[1] < intervals[0][0]:
            res.append(newInterval)
            res.extend(intervals)
            return res
        
        if intervals[-1][1] < newInterval[0]:
            intervals.append(newInterval) 
            return intervals
            
        for i in range(len(intervals)):

            if newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            
            else:
                curr = intervals[i]
                while i<len(intervals) and newInterval[1] >= intervals[i][0]:
                    i += 1
                
                temp = [min(curr[0], newInterval[0]), max(newInterval[1], intervals[i-1][1])]

                res.append(temp)
                break
        
        res.extend(intervals[i:])

        return res



            
            

            
            
