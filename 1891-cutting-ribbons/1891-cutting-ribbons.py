class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        
        l, r = 1, max(ribbons)
        res = 0

        def feasible(length):
            
            totalRibbons = 0
            
            for rib in ribbons:
                totalRibbons += (rib//length) 

            return totalRibbons >= k

        while l <= r:
            
            mid = (l + r) // 2

            if feasible(mid):
                res = max(res, mid)
                l = mid + 1
            
            else:
                r = mid - 1
        
        return res