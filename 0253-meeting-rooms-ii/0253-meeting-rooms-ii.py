class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        start = sorted([s for s,e in intervals])
        end = sorted([e for s,e in intervals])
        j = i = count = 0
        res = 0
        

        while i < len(start):

            if start[i] < end[j]:
                count += 1
                i += 1
            
            else:
                count -= 1
                j += 1
            
            res = max(count, res)
        
        return res