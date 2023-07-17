class DetectSquares:

    def __init__(self):
        self.pointsCount = {}
        self.points = [] 

    def add(self, point: List[int]) -> None:
        self.pointsCount[tuple(point)] = 1 + self.pointsCount.get(tuple(point), 0)
        self.points.append(point)
        
    def count(self, point: List[int]) -> int:
        res = 0
        a, b = point

        for x, y in self.points:
            if (abs(a - x) != abs(b - y)) or a == x or b == y:
                continue
            if (x, b) in self.pointsCount and (a, y) in self.pointsCount:
                res += self.pointsCount[(x, b)] * self.pointsCount[(a, y)]
        
        return res
        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)