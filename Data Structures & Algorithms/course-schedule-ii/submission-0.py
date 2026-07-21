class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # adj list
        adj={c:[] for c in range(numCourses)}

        for crs, pre in prerequisites:
            adj[crs].append(pre)

        res=[]
        vis, cycle=set(), set()

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in vis:
                return True
            
            cycle.add(crs)

            for pre in adj[crs]:
                if dfs(pre) == False:
                    return False
            cycle.remove(crs)
            vis.add(crs)
            res.append(crs)
            return True
        
        for c in range(numCourses):
            if dfs(c) == False:
                return []
        return res