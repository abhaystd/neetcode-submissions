class Solution:
    def row_col_check(self, board: List[List[str]], i: int, j: int) ->bool:
        val = board[i][j]
        # print(i,j)
        # print(val)
        for k in range(0,9):
            if k!=i and val == board[k][j]:
                # print(k," ",board[k][j])
                return False
        for k in range(0,9):
            if k!=j and val == board[i][k]:
                # print(k," ",board[i][k])
                return False
        return True

    def findsquare(self,i,j):
        row_col={"row":0,
                "col":0}
        if i >=0 and i<3:
            row_col['row']=0
        elif i >=3 and i<6:
            row_col['row']=3
        elif i >=6 and i<9:
            row_col['row']=6
        
        if j >=0 and j<3:
            row_col['col']=0
        elif j >=3 and j<6:
            row_col['col']=3
        elif j >=6 and j<9:
            row_col['col']=6
        return row_col

    def check_mini_square(self, board: List[List[str]], i: int, j: int) ->bool:
        val = board[i][j]
        square=self.findsquare(i,j)
        row=square['row']
        col=square['col']

        for k in range(row,row+3):
            for l in range(col,col+3):
                if k!=i and l!=j and val==board[k][l]:
                    # print(k,l,i,j," ",board[k][l])
                    return False
        return True


    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(0,9):
            for j in range(0,9):
                if board[i][j]=='.':
                    continue
                if not self.row_col_check(board,i,j):
                    # print(i,j,'rfalse')
                    return False
                if not self.check_mini_square(board,i,j):
                    # print(i,j,'mfalse')
                    return False
        return True

        