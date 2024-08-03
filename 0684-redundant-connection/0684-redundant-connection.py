class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        par = [i for i in range(len(edges) + 1)]
        rank = [1 for i in range(len(edges) + 1)]

        def findParent(p):
            
            while par[p] != p:
                p = par[p]
            
            return p
        
        def unionFind(node1, node2):
            
            parent1, parent2 = findParent(node1), findParent(node2)

            if parent1 == parent2:
                return False

            if rank[parent1] >= rank[parent2]:
                par[parent2] = parent1
                rank[parent1] += rank[parent2]
            
            else:
                par[parent1] = parent2
                rank[parent2] += rank[parent1]

            return True

        for a, b in edges:
            if not unionFind(a, b):
                return [a, b]
