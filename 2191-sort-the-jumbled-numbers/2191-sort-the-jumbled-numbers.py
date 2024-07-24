class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        
        res = [num for num in nums]
        
        def helper(num):

            newNum = ""

            for n in str(num):
                newNum += str(mapping[int(n)])

            return newNum

        for i, num in enumerate(nums):

            newNum = helper(num)
            res[i] = [int(newNum), i]
        
        arr = [nums[idx] for num, idx in sorted(res)]
        return arr
        
