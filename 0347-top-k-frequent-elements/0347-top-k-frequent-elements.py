class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hashMap = {}
        res, buckets = [], [[] for _ in range(len(nums)+1)]

        for num in nums:
            hashMap[num] = 1 + hashMap.get(num, 0)
        
        for key, val in hashMap.items():
            buckets[val].append(key)

        for sublist in buckets:
            if sublist:
                for num in sublist:
                    res.append(num)

        return res[::-1][:k]

        

        
        