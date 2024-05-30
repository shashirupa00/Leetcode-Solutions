class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        
        pairs.sort(key=lambda x: x[1])
        cur = float("-inf")
        res = 0

        for pair in pairs:
            if pair[0] > cur:
                res += 1
                cur = pair[1]
        
        return res