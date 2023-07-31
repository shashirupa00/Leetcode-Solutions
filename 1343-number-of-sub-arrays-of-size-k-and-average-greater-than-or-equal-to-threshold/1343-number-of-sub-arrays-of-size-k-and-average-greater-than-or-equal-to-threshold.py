class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:

        i, j = 0, k-1
        curSum = sum(arr[i:j+1])
        res = 0

        while True:
            
            if curSum/k >= threshold: res += 1
            
            curSum -= arr[i]
            i += 1

            j += 1
            if j >= len(arr): break
            curSum += arr[j]
        
        return res