class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        edges = defaultdict(list)

        for src, dst in prerequisites:
            edges[src].append(dst)
        
        def dfs(node, visited):
            
            if not len(edges[node]):
                return True
            
            visited.add(node)

            res = True

            for nxt in edges[node]:
                if nxt not in visited:
                    res = res and dfs(nxt, visited)
                else:
                    return False

            visited.remove(node)
            
            return res
            # returns a boolean value
        
        for i in range(numCourses):
            if not dfs(i, set()):
                return False
        
        return True