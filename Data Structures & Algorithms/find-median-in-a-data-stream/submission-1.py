import heapq
class MedianFinder:

    def __init__(self):
        self.max_heap,self.min_heap=[],[]

    def addNum(self, num: int) -> None:
        if self.max_heap and num>self.max_heap[0]:
            heapq.heappush(self.max_heap,num)
        else:
            heapq.heappush(self.min_heap,-1*num)
        if len(self.max_heap)>len(self.min_heap)+1:
            curr=heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap,-1*curr)

        if len(self.min_heap)>len(self.max_heap)+1:
            curr=heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap,-1*curr)

    def findMedian(self) -> float:
        if len(self.min_heap)>len(self.max_heap):
            return -1*self.min_heap[0]
        elif len(self.min_heap)<len(self.max_heap):
            return self.max_heap[0]
        return (-1*self.min_heap[0]+self.max_heap[0])/2
        
        