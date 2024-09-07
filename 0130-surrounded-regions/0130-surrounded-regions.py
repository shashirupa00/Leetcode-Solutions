class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        rows, cols = len(board), len(board[0])
        visited = set()

        def dfs(i, j):
            
            if i not in range(rows) or j not in range(cols) or (i, j) in visited or board[i][j] != 'O':
                return
            
            visited.add((i, j))

            dfs(i + 1, j)
            dfs(i, j + 1)
            dfs(i - 1, j)
            dfs(i, j - 1)

            return

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O' and (i in (0, rows - 1) or j in (0, cols - 1)):
                    dfs(i, j)
        
        print(visited)
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O' and (i, j) not in visited:
                    board[i][j] = 'X'