class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res = []

        def dfs(curr, open, close):

            if open == close == n:
                res.append("".join(curr))
                return
            
            if open >= close and open <= n:
                curr.append('(')
                dfs(curr, open+1, close)
                curr.pop()
            
            if close < open and close <=n:
                curr.append(')')
                dfs(curr, open, close+1)
                curr.pop()
        
        dfs([], 0, 0)

        return res
                


            


        