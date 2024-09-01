class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        
        if m * n > len(original): return []

        i = 0
        res = []

        while i < len(original):
            res.append(original[i: i + n])
            i += n
        
        return res if len(res) == m else []