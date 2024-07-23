class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        
        counter = Counter(nums)
        arr = sorted([(val, key) for key, val in counter.items()], key= lambda x : (x[0], -x[1]))

        res = []

        for val, key in arr:
            res.extend([key] * val)
        
        return res

