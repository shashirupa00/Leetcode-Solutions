class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        res = []
        visited = set()
        count = collections.Counter(nums)

        def dfs(subset):

            if len(subset) == len(nums) and tuple(subset) not in visited:
                res.append(subset[:])
                visited.add(tuple(subset))
                return

            for num in count:
                if count[num] > 0:
                    subset.append(num)
                    count[num] -= 1
                    dfs(subset)
                    temp = subset.pop()
                    count[temp] += 1
            
            return 

        dfs([])

        return res

                
