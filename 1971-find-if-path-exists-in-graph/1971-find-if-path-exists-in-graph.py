class Solution:
    def validPath(
        self, n: int, edges: List[List[int]], source: int, destination: int
    ) -> bool:

        if source == destination: return True

        hashMap = defaultdict(list)
        visited = set()

        for src, dst in edges:
            hashMap[src].append(dst)
            hashMap[dst].append(src)

        def dfs(node):

            if node == destination:
                return True
            
            visited.add(node)

            temp = False

            for nxt in hashMap[node]:
                if nxt not in visited:
                    temp = temp or dfs(nxt)
            
            return temp
        
        return dfs(source)
