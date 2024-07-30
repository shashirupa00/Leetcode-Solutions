class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        hashMap = defaultdict(list)

        for dst, src in prerequisites:
            hashMap[src].append(dst)

        visited = set()
        res = []

        def dfs(node, cycle):
            
            if node in cycle:
                return False
            
            if node in visited:
                return True

            visited.add(node)
            cycle.add(node)

            for nxt in hashMap[node]:
                if not dfs(nxt, cycle):
                    return False
            
            res.append(node)
            cycle.remove(node)

            return True

        for i in range(numCourses):
            if i not in visited:
                if not dfs(i, set()):
                    return []
        
        return res[::-1]