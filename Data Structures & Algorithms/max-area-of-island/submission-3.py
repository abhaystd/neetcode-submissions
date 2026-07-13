class Solution:

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        vis=[[False for _ in range(m)] for _ in range(n)]
        res=0

        def dfs(r,c):
            nonlocal n,m,vis
            if r>=n or c>=m or r<0 or c<0 or grid[r][c]==0 or vis[r][c]:
                return 0
            dirs=[[1,0],[-1,0],[0,1],[0,-1]]
            count=1
            # print(count)
            vis[r][c]=True
            
            for dir in dirs:
                row=r+dir[0]
                col=c+dir[1]
                count+=dfs(row,col)
            return count

        for i in range(n):
            for j in range(m):
                if grid[i][j]==1 and not vis[i][j]:
                    res=max(res,dfs(i,j))
                    
                    
        # TC O(N*M) AND SC (N*M)
        
        return res