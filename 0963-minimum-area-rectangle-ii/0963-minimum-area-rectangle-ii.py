class Solution:
    def minAreaFreeRect(self, points: List[List[int]]) -> float:
        
        rectangles = []
        res = float("inf")

        def dist(i, j):

            x1, y1 = points[i]
            x2, y2 = points[j]

            return sqrt((x2 - x1)**2 + (y2 - y1)**2)

        def slope(point1, point2):
            x1, y1 = points[point1]
            x2, y2 = points[point2]
            if x2 - x1 == 0:
                return float('inf')
            return (y2 - y1) / (x2 - x1)

        def check(x, y):

            p1, p2 = x
            p3, p4 = y


            if len(set([p1, p2, p3, p4])) != 4:
                return False
            
            if dist(p1, p4) != dist(p2, p3) or dist(p1, p3) != dist(p2, p4):
                return False
            
            if slope(p1, p2) != slope(p3, p4):
                return False
            
            if slope(p1, p3) != slope(p2, p4) and slope(p1, p4) != slope(p2, p3):
                return False
            
            if slope(p1, p3) != slope(p2, p4) and dist(p1, p3) != dist(p2, p4):
                return False
            
            if slope(p1, p4) != slope(p2, p3) and dist(p1, p4) != dist(p2, p3) :
                return False
            
            if slope(p1, p3) == slope(p2, p4):
                rectangles.append([dist(p1, p2), dist(p1, p3)])
                return
            
            if slope(p1, p4) == slope(p2, p3):
                rectangles.append([dist(p1, p2), dist(p1, p4)])
                return
                
        hashMap = defaultdict(list)

        for i in range(len(points)):
            for j in range(i+1, len(points)):
                x = dist(i, j)
                for a, b in hashMap[x]:
                    check((a, b), (i, j))
                hashMap[x].append((i, j))
        
        for a, b in rectangles:
            res = min(res, a*b)
        
        return res if res != float("inf") else 0