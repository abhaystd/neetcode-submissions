from collections import defaultdict
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n=len(edges)
        adj=[[] for _ in range(n+1)]
        

        def dfs(node,par):
            if node in vis:
                return True
            vis.add(node)

            for neg in adj[node]:
                if neg==par:
                    continue
                if dfs(neg,node):
                    return True

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
            vis=set()
            if dfs(u,-1):
                return [u,v]
        
        return []
