class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        
        par = {}
        res = []

        def helper(x, y):

            parSet = set()

            for dx, dy in [[0, 1], [1, 0], [-1, 0], [0, -1]]:

                nx, ny = x + dx, y + dy

                if (nx, ny) in par:
                    parSet.add(par[(nx, ny)])
            
            return parSet
        
        for i, position in enumerate(positions):

            curSet = helper(position[0], position[1])

            par[tuple(position)] = i
            
            for key in par:
                if par[key] in curSet:
                    par[key] = i
 
            res.append(len(set(par.values())))
        
        return res