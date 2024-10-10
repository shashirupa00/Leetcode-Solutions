class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        
        newNums = [(num, i) for i, num in enumerate(nums)]
        newNums.sort()
        newNums = [newNum[1] for newNum in newNums] 
        stack = []
        res = 0

        print(newNums)

        for num in newNums:

            while stack and stack[-1] > num:
                stack.pop()

            stack.append(num)
            res = max(res, num - stack[0])

        return res