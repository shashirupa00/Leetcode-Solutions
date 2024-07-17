class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        
        start, end = 0, len(nums) - 1

        hashMap = defaultdict(int)
        res = []

        for end, num in enumerate(nums):

            hashMap[num] += 1

            if end - start == k:

                hashMap[nums[start]] -= 1
                
                if not hashMap[nums[start]]:
                    del hashMap[nums[start]]

                start += 1
            
            if end - start == k - 1:
                count = x
                cur = 0

                for i in range(-50, 0):
                    
                    if i in hashMap:
                        count -= hashMap[i]
                    
                    if count <= 0:
                        cur = i
                        break

                res.append(cur)

        return res