class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        
        if len(bloomDay) < m * k:
            return -1
        
        arr = [i for i in range(min(bloomDay), max(bloomDay) + 1)]
        res = max(bloomDay)

        l, r = 0, len(arr) - 1

        while l <= r:

            mid = (l + r) // 2
            
            curDay = arr[mid]
            boquets = 0
            curFlowers = 0

            for i, num in enumerate(bloomDay):

                if num <= curDay:

                    curFlowers += 1
                
                    if curFlowers == k:
                        boquets += 1
                        curFlowers = 0
                
                else:
                    curFlowers = 0
            
            if boquets >= m:
                res = min(res, curDay)
                r = mid - 1
            
            else:
                l = mid + 1
        
        return res