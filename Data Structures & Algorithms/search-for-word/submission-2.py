class Solution:
    def helper(self,board,k,n,m,i,j,word,vis):
        if k==len(word):
            return True
        if k>len(word) or i>=n or j>=m:
            return False
        
        dirs=[[0,1],[1,0],[0,-1],[-1,0]]
        res=False
        for dir in dirs:
            row=i+dir[0]
            col=j+dir[1]
            if row<n and col <m and row>=0 and col >=0 and not vis[row][col] and board[row][col] == word[k]:
                vis[row][col]=True
  
                res=res or self.helper(board,k+1,n,m,row,col,word,vis)

                vis[row][col]=False
        return res


    def exist(self, board: List[List[str]], word: str) -> bool:
        n=len(board)
        m=len(board[0])
        vis=[[False for _ in range(m)] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                
                if board[i][j]==word[0]:
                    vis[i][j]=True
                    res=self.helper(board,1,n,m,i,j,word,vis)
                    vis[i][j]=False
                    if res:
                        return True
                    
        return False