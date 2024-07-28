class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        rows, cols = len(board), len(board[0])
        visited = set()

        def dfs(i, j):
            
            if not (0 <= i < rows) or not (0 <= j < cols) or (i, j) in visited or board[i][j] == 'X':
                return
            
            visited.add((i, j))

            dfs(i + 1, j)
            dfs(i, j + 1)
            dfs(i - 1, j)
            dfs(i, j - 1)

            return
        
        for j in range(cols):
            dfs(0, j)
            dfs(rows - 1, j)
        
        for i in range(rows):
            dfs(i, 0)
            dfs(i, cols - 1)
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O' and (i, j) not in visited:
                    board[i][j] = 'X'