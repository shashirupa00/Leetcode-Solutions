class Solution:
    def countTheNumOfKFreeSubsets(self, nums: List[int], k: int) -> int:
        
        groups = []
        visited = set()
        nums = set(nums)

        dp = {}

        def fib(n):

            if n == 0: return 1
            if n == 1: return 2
            if n in dp: return dp[n]

            dp[n] = fib(n - 1) + fib(n - 2)
            return dp[n]


        for n in nums:

            temp = []

            if n not in visited:
                
                visited.add(n)
                temp.append(n)

                small, large = n - k, n + k
                
                while small in nums:
                    temp.append(small)
                    visited.add(small)
                    small -= k
                
                while large in nums:
                    temp.append(large)
                    visited.add(large)
                    large += k

            if temp: groups.append(temp)

        res = 1
        for g in groups:
            res *= fib(len(g))
        
        return res