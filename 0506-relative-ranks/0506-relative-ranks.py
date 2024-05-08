class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        
        maxHeap = [(-s, i) for i, s in enumerate(score)]
        heapq.heapify(maxHeap)
        pos = 1

        while maxHeap:
            s, index = heapq.heappop(maxHeap)

            if pos == 1:
                score[index] = "Gold Medal"
            
            elif pos == 2:
                score[index] = "Silver Medal"
            
            elif pos == 3:
                score[index] = "Bronze Medal"
            
            else:
                score[index] = str(pos)
            
            pos += 1
        
        return score
