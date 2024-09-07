class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if len(edges) >= n:
            return False
        
        hashMap = defaultdict(list)

        for a, b in edges:
            hashMap[a].append(b)
            hashMap[b].append(a)
        
        visited = set()

        def dfs(node):
            
            visited.add(node)

            for nxt in hashMap[node]:
                if nxt not in visited:
                    dfs(nxt)

            return
        
        dfs(0)
        
        return len(visited) == n