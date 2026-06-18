import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.n=k
        self.topk=[]
        for num in nums:
            heapq.heappush(self.topk,num)

        while k<len(self.topk):
            heapq.heappop(self.topk)
        
    def add(self, val: int) -> int:
        heapq.heappush(self.topk,val)
        while len(self.topk)>self.n:
            heapq.heappop(self.topk)
        
        return self.topk[0]
        