class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        
        rows, cols = len(matrix), len(matrix[0])
        prefix = [[0 for i in range(cols + 1)] for j in range(rows + 1)]
        res = 0

        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                prefix[i][j] += matrix[i - 1][j - 1] + (prefix[i-1][j] if i - 1 >= 0 else 0)
                prefix[i][j] += (prefix[i][j-1] if j - 1 >= 0 else 0) - (prefix[i-1][j-1] if i - 1 >= 0 and j - 1 >= 0 else 0)
        
        for r1 in range(1, rows + 1):
            for r2 in range(r1, rows + 1):

                hashMap = defaultdict(int)
                hashMap[0] = 1

                for c in range(1, cols + 1):

                    curSum = prefix[r2][c] - prefix[r1 - 1][c]

                    res += hashMap[curSum - target]

                    hashMap[curSum] += 1
        
        return res