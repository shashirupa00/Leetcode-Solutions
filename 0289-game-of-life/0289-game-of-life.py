class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        rows, cols = len(board), len(board[0])
        nextState = []

        def helper(x, y):

            neighbhors = [[0, 1], [1, 0], [0, -1], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]
            totalNeighbhors = 0

            for dx, dy in neighbhors:
                nx, ny = x + dx, y + dy

                if 0 <= nx < rows and 0 <= ny < cols and board[nx][ny]:
                    totalNeighbhors += 1
            
            return totalNeighbhors

        for i in range(rows):
            for j in range(cols):

                totalNeighbhors = helper(i, j)

                if board[i][j] and (totalNeighbhors < 2 or totalNeighbhors > 3):
                    nextState.append([i, j, 0])
                
                if not board[i][j] and (totalNeighbhors == 3):
                    nextState.append([i, j, 1])

        for i, j, state in nextState:
            board[i][j] = state
