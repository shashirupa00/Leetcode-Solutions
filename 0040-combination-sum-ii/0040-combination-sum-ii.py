class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        candidates.sort()

        def dfs(i, sum):

            if sum == target:
                res.append(subset[:])
                return 

            if sum > target or i >= len(candidates):
                return 

            subset.append(candidates[i])
            sum += candidates[i]

            dfs(i+1, sum)

            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1

            sum = sum - subset.pop()

            dfs(i+1, sum)

        dfs(0, 0)

        return res
            
