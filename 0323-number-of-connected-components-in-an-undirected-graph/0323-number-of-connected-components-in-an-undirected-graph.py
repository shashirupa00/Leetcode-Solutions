class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        par = [i for i in range(n)]
        rank = [1 for i in range(n)]

        def findParent(node):
            
            while par[node] != node:
                node = par[node]
            
            return node

        def unionFind(node1, node2):
            
            parent1, parent2 = findParent(node1), findParent(node2)

            if rank[parent1] >= rank[parent2]:
                par[parent2] = parent1
                rank[parent1] += rank[parent2]
            
            else:
                par[parent1] = parent2
                rank[parent2] += rank[parent1]
            
            return
        
        for node1, node2 in edges:
            unionFind(node1, node2)
        
        for i in range(n):
            par[i] = findParent(i)
        
        return len(set(par))