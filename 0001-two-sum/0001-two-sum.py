class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashMap = {}

        for i in range(len(nums)):
            if nums[i] in hashMap.keys():
                return [i, hashMap[nums[i]]]
            hashMap[target - nums[i]] = i


        