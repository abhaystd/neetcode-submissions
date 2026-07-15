class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        n=len(grid)
        m=len(grid[0])

        def dfs(row,col,curr):
            if row<0 or col<0 or row>=n or col>=m or grid[row][col]==-1:
                return

            if curr>grid[row][col]:
                return
                
            grid[row][col]=curr

            dirs=[[-1,0],[1,0],[0,-1],[0,1]]
            for r,c in dirs:
                dfs(row+r,col+c,curr+1)

            return 

        for i in range(n):
            for j in range(m):
                if grid[i][j]==0:
                    dfs(i,j,0)
        # TC O((M*N)^2) AND SC O(M*N)
        return 