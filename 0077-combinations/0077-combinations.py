class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        res = []

        def backTrack(start, arr):

            if len(arr) == k:
                res.append(arr[:])
                return

            for i in range(start, n+1):
                arr.append(i)
                backTrack(i + 1, arr)
                arr.pop()
        
        backTrack(1, [])

        return res 