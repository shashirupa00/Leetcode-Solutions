class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        
        adjList = collections.defaultdict(list)
        revAdjList = collections.defaultdict(list)
        visited = set()
        res = 0 

        for src, dst in connections:
            adjList[src].append(dst)
            revAdjList[dst].append(src)

        def dfs(node):

            nonlocal res

            if node in visited:
                return
            
            visited.add(node)

            for rnxt in revAdjList[node]:
                dfs(rnxt)
            
            for nxt in adjList[node]:
                if nxt not in visited:
                    res += 1
                    dfs(nxt)
            
        dfs(0)

        return res
