# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from queue import PriorityQueue
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res=ListNode(0)
        curr=res
        pq = PriorityQueue()
        count=0
        for i, li in enumerate(lists):
            if li:
                pq.put((li.val,count,li))
                count+=1

        while not pq.empty():

            val,_,nd = pq.get()
            curr.next=nd
            curr=curr.next
            if nd.next:
                pq.put((nd.next.val,count,nd.next))
                count+=1
        return res.next