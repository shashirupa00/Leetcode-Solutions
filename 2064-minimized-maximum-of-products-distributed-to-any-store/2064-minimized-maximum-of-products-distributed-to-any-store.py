class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:

        if len(quantities) == 1: return quantities[0] 
        
        l, r = 1, max(quantities)
        res = max(quantities)

        def check(mid):

            totalStores = 0

            for num in quantities:
                totalStores += math.ceil(num / mid)
            
            return totalStores <= n

        while l <= r:

            mid = (l + r) // 2

            if check(mid):
                r = mid - 1
                res = min(res, mid)
            
            else:
                l = mid + 1
        
        return res