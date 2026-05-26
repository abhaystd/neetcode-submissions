# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        n=0
        curr=head
        while curr:
            curr = curr.next
            n+=1
        mid=(n+1)//2
        curr=head
        # dividing into two 
        while mid>1:
            curr=curr.next
            mid-=1
        
        second=curr.next
        curr.next=None
        # reverse second  linked list
        prev=None
        while second:
            nxt=second.next
            second.next=prev
            prev=second
            second=nxt

        first = head
        second = prev
        while second:
            nxt1=first.next
            nxt2=second.next

            first.next=second
            second.next=nxt1

            first = nxt1
            second=nxt2


            



        
