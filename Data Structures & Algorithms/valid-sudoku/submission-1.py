class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # using has map
        row=defaultdict(set)
        col=defaultdict(set)
        squares=defaultdict(set) #key = (row//3,col//3)
        for i in range(0,9):
            for j in range(0,9):
                if board[i][j]=='.':
                    continue
                if (board[i][j] in row[i] or board[i][j] in col[j]
                    or board[i][j] in squares[(i//3,j//3)]):
                    return False
                row[i].add(board[i][j])
                col[j].add(board[i][j])
                squares[(i//3,j//3)].add(board[i][j])
        return True

        