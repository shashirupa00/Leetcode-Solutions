class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        hashMap = {i : [] for i in range(numCourses)}
        visited, cycle = set(), set()
        res = []

        for course, prereq in prerequisites:
            hashMap[course].append(prereq)

        
        def dfs(course):

            if course in cycle:
                return False
            
            if course in visited:
                return True
            
            cycle.add(course)

            for crs in hashMap[course]:
                if not dfs(crs): return False
            
            visited.add(course)
            cycle.remove(course)
            res.append(course)

            return True
            
        for crs in range(numCourses):

            if not dfs(crs): return []
        
        return res


        