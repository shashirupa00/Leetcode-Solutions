class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if len(edges) != n - 1: return False
    
        hashMap = defaultdict(list)
        visited = set()

        for src, dst in edges:
            hashMap[src].append(dst)
            hashMap[dst].append(src)
        
        def dfs(node):
            
            if node in visited: return
            visited.add(node)
            for nxt in hashMap[node]:
                dfs(nxt)

        dfs(0)

        return len(visited) == n