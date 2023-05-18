class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        res = []
        board = [['.' for _ in range(n)] for _ in range(n)]
        cols = set()
        pDiag = set()
        nDiag = set()

        def dfs(i):

            if i == n:
                c = ["".join(board[i]) for i in range(n)]
                res.append(c[:])
                return 

            for j in range(n):
                if j in cols or (i+j) in pDiag or (i-j) in nDiag:
                    continue

                cols.add(j)  
                pDiag.add(i+j)
                nDiag.add(i-j)
                

                board[i][j] = 'Q'
                dfs(i+1)

                cols.remove(j)   
                pDiag.remove(i+j)
                nDiag.remove(i-j)
                board[i][j] = '.'


            return

        dfs(0)

        return res  





        