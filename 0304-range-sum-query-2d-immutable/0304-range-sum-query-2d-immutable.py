class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.preMat = [[0] * (len(matrix[0]) + 1) for _ in range(len(matrix) + 1)]
        for i, line in enumerate(matrix):
            previous = 0
            for j, num in enumerate(line):
                previous += num
                above = self.preMat[i][j + 1]
                self.preMat[i + 1][j + 1] = previous + above

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r1, c1, r2, c2 = row1+1, col1+1, row2+1, col2+1

        return (self.preMat[r2][c2] - self.preMat[r2][c1-1] - self.preMat[r1-1][c2] + self.preMat[r1-1][c1-1])        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)