class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:

        adjList = collections.defaultdict(list)
        res = float("inf")
        parent = [i for i in range(n+1)]
        rank = [1 for i in range(n+1)]

        for src, dst, distance in roads:
            adjList[src].append(dst)
            adjList[dst].append(src)

        def findParent(p):

            while parent[p] != p:
                p = parent[p]

            return p
        
        def findRank(n1, n2): 

            p1, p2 = findParent(n1), findParent(n2)

            if p1 == p2:
                return

            if rank[p1] >= rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]
               
        for i in range(1, n+1):
            for j in adjList[i]:
                findRank(i, j)
      
        for i in range(len(parent)):
            parent[i] = findParent(parent[i])

        mainParent = parent[1]
        newAdjList = collections.defaultdict(list)

        for src, dst, distance in roads:
            if parent[src] == mainParent or parent[dst] == mainParent:
                newAdjList[src].append([dst, distance])
        
        for key in newAdjList.keys():
            for dst, distance in newAdjList[key]:
                res = min(res, distance)

        return res