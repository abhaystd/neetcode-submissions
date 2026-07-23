class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        vis=set()
        adj = [[] for _ in range(n)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(crs):
            if crs in vis:
                return
            vis.add(crs)

            for node in adj[crs]:
                dfs(node)
            return

        res=0

        for node in range(n):
            if node not in vis:
                
                dfs(node)
                res+=1

        return res