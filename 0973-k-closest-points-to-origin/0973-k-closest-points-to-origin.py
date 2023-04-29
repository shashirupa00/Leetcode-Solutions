class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        distances, res = [], []
        hashMap = collections.defaultdict(list)
        
        for x, y in points:
            d = math.sqrt((x*x) + (y*y))
            hashMap[d].append([x,y])
            distances.append(d)

        heapq.heapify(distances)

        for i in range(k):
            temp = heapq.heappop(distances)
            tmp = hashMap[temp].pop()
            res.append(tmp)
            
        return res


        