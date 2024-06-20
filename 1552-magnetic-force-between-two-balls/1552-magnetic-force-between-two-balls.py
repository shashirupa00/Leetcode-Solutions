class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        
        position.sort()

        def check(mid):

            balls = 1
            start = position[0]

            for i in range(1, len(position)):

                if position[i] - start >= mid:
                    balls += 1
                    start = position[i]
            
            return balls >= m

        l, r = 0, position[-1]
        res = 0

        while l <= r:

            mid = (l + r) // 2

            if check(mid):
                l = mid + 1
                res = max(res, mid)
            
            else:
                r = mid - 1
        
        return res
