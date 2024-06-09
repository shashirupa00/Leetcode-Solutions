class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        
        hashMap = defaultdict(int)
        prefix = 0
        res = 0

        hashMap[0] = 1

        for i, num in enumerate(nums):

            prefix += num
            remainder = prefix % k

            if remainder in hashMap:
                res += hashMap[remainder]

            hashMap[remainder] += 1
        
        return res

            
