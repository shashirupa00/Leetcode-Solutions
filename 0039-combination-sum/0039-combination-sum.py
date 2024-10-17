class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []

        def backTrack(i, arr):
            
            if sum(arr) >= target or i >= len(candidates):

                if sum(arr) == target:
                    res.append(arr[:])

                return
            
            backTrack(i, arr + [candidates[i]])
            backTrack(i + 1, arr)

            return

        backTrack(0, [])
        return res