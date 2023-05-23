class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        par = [i for i in range(len(edges)+1)]
        rank = [1 for i in range(len(edges)+1)]

        def find(p):
          
            while p != par[p]:
                p = par[p]
            
            return p
        
        def union(n1, n2):

            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return False
            
            elif rank[p1] >= rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]

            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            
            return True

        for s, e in edges:
            if not union(s,e): return [s,e]
        

            


        