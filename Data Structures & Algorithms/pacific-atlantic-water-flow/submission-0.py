class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res=[]
        n=len(heights)
        m=len(heights[0])
        a=set()
        p=set()
        def dfs(row,col,visit,val):
            if ((row,col) in visit) or row<0 or col<0 or row>=n or col>=m or heights[row][col] < val:
                return

            visit.add((row,col))
            dfs(row+1,col,visit,heights[row][col])
            dfs(row-1,col,visit,heights[row][col]) 
            dfs(row,col+1,visit,heights[row][col]) 
            dfs(row,col-1,visit,heights[row][col])
            

        for c in range(m):
            dfs(0,c,p,heights[0][c])
            dfs(n-1,c,a,heights[n-1][c])

        for r in range(n):
            dfs(r,0,p,heights[r][0])
            dfs(r,m-1,a,heights[r][m-1])
        
        for i in range(n):
            for j in range(m):
                if (i,j) in a and (i,j) in p:
                    res.append([i,j])

        return res
