class Solution:
    def minEatingSpeed(self, piles: List[int], hours: int) -> int:

        minK = float("inf")
        l, h = 1, max(piles)

        while l <= h:
            
            mid = (l+h)//2
            time = 0

            for i in range(len(piles)):
                time += math.ceil(piles[i]/mid)
            
            if time <= hours:
                minK = min(minK, mid)
                h = mid -1
            
            else:
                l = mid +1

        return minK

            




        








        