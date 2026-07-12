class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n=len(grid)
        m=len(grid[0])
        vis=[[False for _ in range(m)] for _ in range(n)]
        res=0

        def dfs(r,c):
            nonlocal n,m,vis,res
            if r>=n or c>=m or r<0 or c<0 or grid[r][c]=='0':
                return
            
            dirs=[[1,0],[-1,0],[0,1],[0,-1]]
            for dir in dirs:
                row=r+dir[0]
                col=c+dir[1]
                if row<n and col<m and row>=0 and col>=0 and grid[row][col]=='1' and not vis[row][col]:
                    vis[row][col]=True
                    dfs(row,col)

        for i in range(n):
            for j in range(m):
                if grid[i][j]=='1' and not vis[i][j]:
                    dfs(i,j)
                    res+=1
        # TC O(N*M) AND SC (N*M)
        
        return res