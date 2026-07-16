class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        fill=[]
        for row in range(n):
            r=[]
            for col in range(m):
                val= -1 
                if grid[row][col] == 2:
                    val = 0
                elif  grid[row][col] == 1:
                    val=float('inf')
                r.append(val)
            fill.append(r)
        
        def dfs(row,col,t):
            if row<0 or col<0 or row>=n or col>=m or fill[row][col]==-1:
                return
            
            if fill[row][col]<t:
                return
            fill[row][col]=t
            dfs(row+1,col,t+1)
            dfs(row,col+1,t+1)
            dfs(row-1,col,t+1)
            dfs(row,col-1,t+1)
            return

        for r in range(n):
            for c in range(m):
                if fill[r][c]==0:
                    dfs(r,c,0)
        res=0
        for r in range(n):
            for c in range(m):
                if fill[r][c]==float('inf'):
                    return -1
                if fill[r][c]!=0 and fill[r][c]!=-1:
                    res=max(res,fill[r][c])
        return res