class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        
        edges = []

        for i in range(len(stones)):
            for j in range(i + 1, len(stones)):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    edges.append((i, j))
        
        par = [i for i in range(len(stones))]
        rank = [1 for i in range(len(stones))]

        def findParent(p):

            while par[p] != p:
                p = par[p]

            return p

        def unionFind(n1, n2):
            
            print(n1, n2)
            p1, p2 = findParent(n1), findParent(n2)

            if p1 == p2:
                return

            if rank[p1] >= rank[p2]:
                rank[p1] += rank[p2]
                par[p2] = p1

            else:
                rank[p2] += rank[p1]
                par[p1] = p2

        for a, b in edges:
            unionFind(a, b)
        
        for i in range(len(stones)):
            findParent(i)
        
        counter = collections.Counter(par)
        res = 0

        for key, val in counter.items():
            res += val - 1
        
        return res