class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        intervals.append(newInterval)
        intervals.sort()

        res = []

        for i in range(len(intervals)):

            cur = intervals[i]

            if res and res[-1][0] <= cur[0] <= res[-1][1]:
                temp = res.pop()
                cur = [min(temp[0], cur[0]), max(temp[1], cur[1])]
            
            res.append(cur)
        
        return res