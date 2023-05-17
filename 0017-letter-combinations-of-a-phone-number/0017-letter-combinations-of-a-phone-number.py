class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if digits == "":
            return []

        res = []
        hashMap = {"1": '', "2": 'abc',"3": 'def',"4": 'ghi',"5": 'jkl',"6": 'mno',"7": 'pqrs',"8": 'tuv',"9": 'wxyz'}
        s = []

        def dfs(i):

            if len(s) == len(digits):
                res.append("".join(s))
                return

            for j in range(len(hashMap[digits[i]])):
                s.append(hashMap[digits[i]][j])
                dfs(i+1)
                s.pop()
            
            return
        
        dfs(0)
        return res



        




        