class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        if len(piles) == 1:
            return math.ceil(piles[0]/h)
            
        low, high = 1, max(piles)
        newMin = float("inf")

        while low<=high:

            mid = (low+high)//2
            temp = 0

            for p in piles:
                temp += math.ceil(p/mid) 
            
            if temp<=h:
                newMin = min(newMin, mid)
                high = mid-1
            
            else:
                low = mid+1
        
        return int(newMin)

