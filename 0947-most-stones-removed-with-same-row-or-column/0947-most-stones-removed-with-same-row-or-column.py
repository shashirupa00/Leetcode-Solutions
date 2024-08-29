class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        
        edges = []

        for i in range(len(stones)):
            for j in range(i + 1, len(stones)):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    edges.append((i, j))
        
        par = [i for i in range(len(stones))]
        rank = [1 for i in range(len(stones))]

        print(edges)

        def findParent(node):
            
            while par[node] != node:
                node = par[node]
            
            return node

        def unionFind(node1, node2):
            
            parent1, parent2 = findParent(node1), findParent(node2)

            if parent1 == parent2:
                return

            if rank[parent1] >= rank[parent2]:
                par[parent2] = parent1
                rank[parent1] += rank[parent2]
            
            else:
                par[parent1] = parent2
                rank[parent2] += rank[parent1]
            
            return

        for a, b in edges:
            unionFind(a, b)
        
        for i in range(len(stones)):
            par[i] = findParent(i)
        
        counter = collections.Counter(par)
        res = 0

        for key, val in counter.items():
            res += val - 1
        
        return res