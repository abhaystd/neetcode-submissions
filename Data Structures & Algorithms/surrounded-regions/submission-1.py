class Solution:
    def solve(self, board: List[List[str]]) -> None:
        exclude=set()
        n=len(board)
        m=len(board[0])
        # for i in range(n):
        #     if board[i][0]=='O':
        #         exclude.add((i,0))
        #     if board[i][m-1]=='O':
        #         exclude.add((i,m-1))
            
        # for i in range(m):
        #     if board[0][i]=='O':
        #         exclude.add((0,i))
        #     if board[n-1][i]=='O':
        #         exclude.add((n-1,i))
            
        def dfs(row,col):
            if row<0 or col<0 or row>=n or col>=m or board[row][col]=='X' or (row,col) in exclude:
                return 

            exclude.add((row,col))

            dirs=[[1,0],[-1,0],[0,1],[0,-1]]
            for r,c in dirs:
                dfs(row+r,col+c)
            return

        # for i in range(n):
        #     for j in range(m):
        #         if board[i][j]=='O' and (i,j) in exclude:
        #             dfs(i,j)

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
                if board[i][j]=='O' and (i,j) not in exclude:
                    board[i][j]='X'
        return