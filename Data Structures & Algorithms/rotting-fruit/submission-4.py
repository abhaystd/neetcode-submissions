from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])

        queue=deque()
        fresh=0
        time=0
        for row in range(n):
            for col in range(m):
                if grid[row][col]==2:
                    queue.append((row,col))
                if grid[row][col]==1:
                    fresh+=1
        dirs=[[1,0],[-1,0],[0,1],[0,-1]]
        while queue and fresh:
            q=len(queue)
            for i in range(q):
                r,c=queue.popleft()
                for i,j in dirs:
                    row=r+i
                    col=c+j
                    if (row>=0 and col>=0 and row<n and col<m and grid[row][col]==1):
                        grid[row][col]=2
                        queue.append((row,col))
                        fresh-=1
            time+=1

        # TC O(M*N) AND SC (M*N)
        return time if not fresh else -1
