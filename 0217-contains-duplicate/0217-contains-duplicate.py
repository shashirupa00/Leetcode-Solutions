class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        hashMap = {}

        for num in nums:
            hashMap[num] = 1 + hashMap.get(num, 0)
            if hashMap[num] > 1:
                return True

        return False
        