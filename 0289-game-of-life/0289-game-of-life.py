class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        rows, cols = len(board), len(board[0])
        
        nextState = set()
        nei = [[0, 1], [1, 0], [0, -1], [-1, 0], [1, 1], [-1, -1], [-1, 1], [1, -1]]

        for i in range(len(board)):
            for j in range(len(board[0])):
                
                live = True if board[i][j] else False
                totalNeighbors = 0
                
                for di, dj in nei:
                    ni, nj = i + di, j + dj
                    if ni in range(rows) and nj in range(cols) and board[ni][nj]:
                        totalNeighbors += 1
                
                if live and (totalNeighbors == 2 or totalNeighbors == 3):
                    nextState.add((i, j))

                if not live and totalNeighbors == 3:
                    nextState.add((i, j))
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j] = 1 if (i, j) in nextState else 0
            
