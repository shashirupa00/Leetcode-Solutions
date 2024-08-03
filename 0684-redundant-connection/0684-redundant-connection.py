class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        par = [i for i in range(len(edges)+1)]
        rank = [1 for i in range(len(edges)+1)]

        def findParent(node):

            while par[node] != node:
                node = par[node]
            
            return node
        
        def findRank(a, b):

            p1, p2 = findParent(a), findParent(b)

            if p1 == p2:
                return False

            if rank[p1] >= rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            
            else:
                par[p1]= p2
                rank[p2] += rank[p1]
            
            return True
                
        
        for a, b in edges:
            if not findRank(a, b): return [a, b]


            



