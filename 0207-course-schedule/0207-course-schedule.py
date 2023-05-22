class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        if not prerequisites:
            return True 

        hashMap = collections.defaultdict(list)
        visited = set()

        for i in range(numCourses):
            hashMap[i] = []

        for a, b in prerequisites:
            hashMap[a].append(b) 

        def dfs(course):
            if course in visited:
                return False
            
            if hashMap[course] == []:
                return True
            
            visited.add(course)

            for i in range(len(hashMap[course])):
                
                if not dfs(hashMap[course][i]):
                    return False
            
            visited.remove(course)
            hashMap[course] = []

            return True
                                    
        for c in range(numCourses):
            if not dfs(c): return False

        return True


        