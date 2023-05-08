class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        longestStreak = 0
        numSet = set(nums)

        for num in numSet:

            if num-1 not in numSet:
                curr = num
                currStreak = 1

                while curr+1 in numSet:
                    curr = curr+1
                    currStreak += 1
                
                longestStreak = max(longestStreak, currStreak)

        return longestStreak


        