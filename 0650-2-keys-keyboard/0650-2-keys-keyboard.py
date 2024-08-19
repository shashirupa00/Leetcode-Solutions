class Solution:
    def minSteps(self, n: int) -> int:

        res = float("inf")

        if n == 1: return 0
        
        @cache
        def dfs(cur, prev, inst, tries):

            nonlocal res

            if cur > n:
                return 
            
            if cur == n:
                res = min(res, tries)
                return
            
            if inst == 'c':
                dfs(cur+cur, cur, 'p', tries+1)
            
            else:
                dfs(cur+prev, prev, 'p', tries+1)
                dfs(cur, cur, 'c', tries+1)
            
            return 
        
        dfs(1, 0, 'c', 1)
        return res