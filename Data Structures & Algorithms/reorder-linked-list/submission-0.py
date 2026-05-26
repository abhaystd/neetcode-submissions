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

        curr = head
        while (curr or prev):

            nxt=curr.next
            if prev:
                curr.next = prev
                prev=prev.next
                curr=curr.next
            curr.next=nxt
            curr=curr.next

            



        
