class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        
        res = 0
        start = 0
        maxDeq, minDeq = collections.deque([]), collections.deque([])

        for end in range(len(nums)):

            while maxDeq and maxDeq[-1] < nums[end]:
                maxDeq.pop()
            
            maxDeq.append(nums[end])

            while minDeq and minDeq[-1] > nums[end]:
                minDeq.pop()
            
            minDeq.append(nums[end])

            while minDeq and maxDeq and maxDeq[0] - minDeq[0] > limit:

                if minDeq[0] == nums[start]:
                    minDeq.popleft()
                if maxDeq[0] == nums[start]:
                    maxDeq.popleft()
                start += 1
            
            res = max(end - start + 1, res)
        
        return res