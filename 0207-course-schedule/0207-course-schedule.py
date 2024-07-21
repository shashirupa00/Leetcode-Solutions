class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        edges = defaultdict(list)
        visited = set()

        for src, dst in prerequisites:
            edges[src].append(dst)
        
        def dfs(node, cycle):
            
            if not len(edges[node]) or node in visited:
                return True
            
            cycle.add(node)
            visited.add(node)

            res = True

            for nxt in edges[node]:
                if nxt not in cycle:
                    res = res and dfs(nxt, cycle)
                else:
                    return False
            
            cycle.remove(node)
            
            return res
        
        for i in range(numCourses):
            if not dfs(i, set()):
                return False
        
        return True