class Solution:
    def maximumInvitations(self, grid: List[List[int]]) -> int:
        
        rows, cols = len(grid), len(grid[0])
        hashMap = {}

        def backTrack(i, visited):
            
            for j in range(cols):

                if grid[i][j] and j not in visited:
                    visited.add(j)

                    if j not in hashMap or backTrack(hashMap[j], visited):
                        hashMap[j] = i
                        return True
                    
            return
        

        for i in range(rows):
            backTrack(i, set())
        
        return len(hashMap)