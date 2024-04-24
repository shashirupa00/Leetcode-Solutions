class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        
        hashMap = defaultdict(list)
        pattern = defaultdict(int)

        for u, t, w in zip(username, timestamp, website):
            hashMap[u].append((t, w))
        
        for u in hashMap:
            hashMap[u].sort()
        

        for u in hashMap:
            if len(hashMap[u]) >= 3:
                for i in range(len(hashMap[u])):
                    p1 = hashMap[u][i][1]
                    for j in range(i+1, len(hashMap[u])):
                        p2 = hashMap[u][j][1]
                        for k in range(j+1, len(hashMap[u])):
                            p3 = hashMap[u][k][1]
                            pattern[(p1, p2, p3)] += 1

        res, maxVal = [], 0

        print(pattern)

        for key in pattern:
            if pattern[key] >= maxVal:
                if not res:
                    res = key
                else:
                    res = min(res, key)
                maxVal = pattern[key]

        return list(res)