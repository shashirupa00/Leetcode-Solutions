class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        hashMap = collections.Counter(nums)
        k = len(nums) - hashMap[val]

        while val in nums:
            nums.remove(val)
        
        return k
        