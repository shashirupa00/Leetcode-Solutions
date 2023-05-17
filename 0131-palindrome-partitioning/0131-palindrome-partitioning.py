class Solution:
    def partition(self, s: str) -> List[List[str]]:

        res = []
        subset = []

        def dfs(i):
            if i >= len(s):
                res.append(subset[:])
                return
            
            for j in range(i, len(s)):
                if s[i:j+1] == s[i:j+1][::-1]:
                    subset.append(s[i:j+1])
                    dfs(j+1)
                    subset.pop()

            return
        
        dfs(0)
        return res