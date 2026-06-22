import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        q=[]
        for i in range(len(points)):
            a=points[i][0]*points[i][0]
            b=points[i][1]*points[i][1]
            dis=math.sqrt(a+b)
            heapq.heappush(q,(-dis,points[i]))
        # print(q)
        while len(q)>k:
            heapq.heappop(q)
        # print(q)
        res=[]
        while len(q):
            curr=heapq.heappop(q)[1]
            res.append(curr)
        return res