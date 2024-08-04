class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []

        def backTrack(cur, openCount):
            
            if len(cur) >= n*2:
                if openCount == 0:
                    res.append(cur[:])
                return
            
            backTrack(cur + "(", openCount + 1)

            if openCount > 0:
                backTrack(cur + ")", openCount - 1)

            return
        
        backTrack("", 0)

        return res