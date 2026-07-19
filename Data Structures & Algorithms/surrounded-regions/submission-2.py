class Solution:
    def solve(self, board: List[List[str]]) -> None:
        n=len(board)
        m=len(board[0])

        def dfs(row,col):
            if row<0 or col<0 or row>=n or col>=m or board[row][col]=='X' or board[row][col]=='#':
                return 

            board[row][col]='#'

            dirs=[[1,0],[-1,0],[0,1],[0,-1]]
            for r,c in dirs:
                dfs(row+r,col+c)
            return

        for i in range(n):
            if board[i][0]=='O':
                dfs(i,0)
            if board[i][m-1]=='O':
                dfs(i,m-1)
            
        for i in range(m):
            if board[0][i]=='O':
                dfs(0,i)
            if board[n-1][i]=='O':
                dfs(n-1,i)

        for i in range(n):
            for j in range(m):
                if board[i][j]=='O':
                    board[i][j]='X'
                
        for i in range(n):
            for j in range(m):
                if board[i][j]=='#':
                    board[i][j]='O'

        return