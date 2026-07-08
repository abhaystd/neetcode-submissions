class Solution:
    def __init__(self):
        self.res=[]
    def is_safe(self,n,board,row,i):
        r=row-1
        while r>=0:
            if board[r][i]=='Q':
                return False
            r-=1

        r=row-1
        c=i-1
        while r>=0 and c>=0:
            if board[r][c]=='Q':
                return False
            r-=1
            c-=1
        r=row-1
        c=i+1
        while r>=0 and c<n:
            if board[r][c]=='Q':
                return False
            r-=1
            c+=1
        return True
    def queenBoard(self,n,board,row):
        if row==n:
            copy=[''.join(row) for row in board]
            self.res.append(copy)
            return
        for col in range(n):
            if self.is_safe(n,board,row,col):
                board[row][col]='Q'
                self.queenBoard(n,board,row+1)
                board[row][col]='.'
        return
    def solveNQueens(self, n: int) -> List[List[str]]:
        board=[['.']*n for i in range(n)]
        self.queenBoard(n,board,0)
        return self.res