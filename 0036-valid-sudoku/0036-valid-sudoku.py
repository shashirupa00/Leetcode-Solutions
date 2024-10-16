class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows, cols = 9, 9
        rowMap, colMap, boxMap = defaultdict(set), defaultdict(set), defaultdict(set)

        for i in range(rows):
            for j in range(cols):

                if board[i][j] != '.':

                    if board[i][j] in rowMap[i] or board[i][j] in colMap[j] or board[i][j] in boxMap[(i//3, j//3)]:
                        return False
                    
                    rowMap[i].add(board[i][j])
                    colMap[j].add(board[i][j])
                    boxMap[(i//3, j//3)].add(board[i][j])
        
        return True
