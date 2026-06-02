# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from queue import PriorityQueue
class Solution: 
    def conqure(self,left,right):
        res=ListNode(0)
        curr=res
        while left and right:
            if left.val<=right.val:
                curr.next=left
                left=left.next
            else:
                curr.next=right
                right=right.next
            curr=curr.next
        if left:
            curr.next=left
        if right:
            curr.next=right
        return res.next
               
    def divide(self,lists: List[Optional[ListNode]],l:int, r:int)->Optional[ListNode]:

        if l>r:
            return None
        if l == r:
            return lists[l]
        mid = (l+r)//2
        left  = self.divide(lists,l,mid)
        right = self.divide(lists,mid+1,r)

        return self.conqure(left,right)

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) ==0:
            return None

        return self.divide(lists,0,len(lists)-1)