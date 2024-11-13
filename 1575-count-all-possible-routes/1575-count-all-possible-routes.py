class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        
        dp = defaultdict(int)

        def backTrack(i, fuel):
            
            if (i, fuel) in dp:
                return dp[(i, fuel)]

            if i == finish:
                dp[(i, fuel)] += 1

            for j in range(len(locations)):

                if i != j and abs(locations[i] - locations[j]) <= fuel:
                    dp[(i, fuel)] += backTrack(j, fuel - abs(locations[i] - locations[j]))
            
            return dp[(i, fuel)]

        
        return backTrack(start, fuel)