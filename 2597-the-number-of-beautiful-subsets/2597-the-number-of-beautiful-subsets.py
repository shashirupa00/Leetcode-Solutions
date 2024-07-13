class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        
        hashMap = defaultdict(int)

        def dfs(i):

            if i == len(nums):
                return 1
            
            res = dfs(i + 1)

            if not hashMap[nums[i] - k] and not hashMap[nums[i] + k]:
                hashMap[nums[i]] += 1
                res += dfs(i + 1)
                hashMap[nums[i]] -= 1
            
            return res
        
        return dfs(0) - 1