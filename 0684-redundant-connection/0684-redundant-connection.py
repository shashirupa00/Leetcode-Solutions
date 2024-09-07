class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        par = [i for i in range(len(edges) + 1)]
        rank = [1 for i in range(len(edges) + 1)]

        def findParent(node):
            while node != par[node]:
                node = par[node]
            return node
        
        def unionFind(n1, n2):
            
            p1, p2 = findParent(n1), findParent(n2)

            if p1 == p2:
                return False
            
            if rank[p1] > rank[p2]:
                rank[p1] += rank[p2]
                par[p2] = p1
            
            else:
                rank[p2] += rank[p1]
                par[p1] = p2
            
            return True
        
        for a, b in edges:
            if not unionFind(a, b):
                return [a, b]