class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []

        def backTrack(cur, count):
            
            if len(cur) > n * 2 or count < 0 or count > n:
                return False
            
            if not count and len(cur) == n * 2:
                res.append(cur[:])
            
            backTrack(cur + "(", count + 1)
            backTrack(cur + ")", count - 1)

            return

        backTrack("", 0)
        return res