class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l, r = 1, max(piles)

        while l <= r:

            mid = (l + r) // 2

            curHours = 0
            for i in range(len(piles)):
                curHours += math.ceil(piles[i] / mid)
            
            if curHours <= h:
                r = mid - 1
            
            else:
                l = mid + 1
        
        return l