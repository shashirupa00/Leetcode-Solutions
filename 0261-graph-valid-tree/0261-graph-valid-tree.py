class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        par = [i for i in range(n)]
        rank = [1 for i in range(n)]

        def find(p):
            while p != par[p]:
                p = par[p]
            return p

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return
            
            elif rank[p1] >= rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
        
        for a,b in edges:
            union(a,b)
        
        for i in range(len(par)):
            par[i] = find(par[i])       


        return len(set(par)) == 1 and n-1 == len(edges)