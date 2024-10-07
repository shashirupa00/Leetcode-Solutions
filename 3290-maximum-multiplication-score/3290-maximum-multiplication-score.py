class Solution:
    def maxScore(self, a: List[int], b: List[int]) -> int:
        
        max_score = float("-inf")
        
        for indices in combinations(range(len(b)), 4):
            score = a[0] * b[indices[0]] + a[1] * b[indices[1]] + a[2] * b[indices[2]] + a[3] * b[indices[3]]
            max_score = max(max_score, score)
        
        return max_score