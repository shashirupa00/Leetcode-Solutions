class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        
        minDeq, maxDeq = collections.deque([]), collections.deque([])
        l = 0
        res = 0

        for r in range(len(nums)):

            while maxDeq and maxDeq[-1] < nums[r]:
                maxDeq.pop()
            maxDeq.append(nums[r])

            while minDeq and minDeq[-1] > nums[r]:
                minDeq.pop()
            minDeq.append(nums[r])

            while maxDeq[0] - minDeq[0] > limit:

                if nums[l] == maxDeq[0]:
                    maxDeq.popleft()
                
                if nums[l] == minDeq[0]:
                    minDeq.popleft()
                
                l += 1
            
            res = max(res, r - l + 1)
        
        return res
            