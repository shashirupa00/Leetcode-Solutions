class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        
        res = []

        def backTrack(num):

            if num > n:
                return
            
            res.append(num)
            
            for i in range(10):
                backTrack((num * 10) + i)

            return
        
        for i in range(1, 10):
            backTrack(i)

        return res