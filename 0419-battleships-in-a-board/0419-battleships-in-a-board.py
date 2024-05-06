class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        
        visited = set()
        rows, cols = len(board), len(board[0])
        res = 0

        def check(i, j):
            return True if i in range(rows) and j in range(cols) else False

        def dfs(i, j, direction):
            
            if not check(i, j) or (i, j) in visited or board[i][j] != "X":
                return False
            
            visited.add((i, j))

            x, y = direction

            dfs(i+x, j+y, direction)


        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "X" and (i, j) not in visited:
                    if check(i + 1, j) and board[i+1][j] == "X":
                        dfs(i, j, (1, 0))
                    if check(i, j + 1) and board[i][j+1] == "X":
                        dfs(i, j, (0, 1))
                    res += 1
        
        return res