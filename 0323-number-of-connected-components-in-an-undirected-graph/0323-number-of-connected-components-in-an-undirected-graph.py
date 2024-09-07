class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        visited = set()
        hashMap = defaultdict(list)
        res = 0

        for src, dst in edges:
            hashMap[src].append(dst)
            hashMap[dst].append(src)

        def dfs(node):
            
            visited.add(node)

            for nxt in hashMap[node]:
                if nxt not in visited:
                    dfs(nxt)
        
        for node in range(n):
            if node not in visited:
                res += 1
                dfs(node)
        
        return res