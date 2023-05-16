class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        n = len(word)
        path = set()
        
        def dfs(i, j, c):

            if c == len(word):
                return True

            if (i < 0 or j < 0 or 
               c >= n or c >= n or 
               ((i,j) in path) or
               i>=len(board) or j >=len(board[0])
               or board[i][j] != word[c]):
                
                return False
            
            path.add((i,j))
            res = (dfs(i+1, j, c+1) or
                dfs(i-1, j, c+1) or
                dfs(i, j+1, c+1) or
                dfs(i, j-1, c+1))
            path.remove((i,j))
               
            return res

        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0):
                    return True
        
        return False

            

