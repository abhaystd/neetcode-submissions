import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h=[]
        for st in stones:
            heapq.heappush(h,-st)
        
        while len(h)>1:
            firststone=abs(heapq.heappop(h))
            secondstone=abs(heapq.heappop(h))
            if firststone!=secondstone:
                heapq.heappush(h,-abs(firststone-secondstone))
        # tc O(nlogn)  and sc O(n)
        return abs(h[0]) if len(h)>0 else 0

