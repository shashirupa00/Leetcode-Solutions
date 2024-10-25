class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        hashMap = defaultdict(list)
        visited = set()
        res = []

        for src, dst in prerequisites:
            hashMap[src].append(dst)

        
        def dfs(course, cycle):
            
            if course in cycle:
                return False
            
            if course in visited:
                return True
            
            visited.add(course)
            cycle.add(course)

            for nxt in hashMap[course]:
                if not dfs(nxt, cycle):
                    return False
            
            res.append(course)
            cycle.remove(course)

            return True
        
        for i in range(numCourses):
            if i not in visited:
                if not dfs(i, set()):
                    return []
        
        return res if len(visited) == numCourses else []