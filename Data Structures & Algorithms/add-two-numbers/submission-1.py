# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry=0
        res=ListNode(0)
        curr=res
        while l1 and l2:
            value=l1.val+l2.val+carry
            listval=value%10
            carry=value//10
            newNode= ListNode(listval)
            curr.next=newNode
            curr=curr.next
            l1=l1.next
            l2=l2.next
        
        while l1:
            value=l1.val+carry
            listval=value%10
            carry=value//10
            newNode= ListNode(listval)
            curr.next=newNode
            curr=curr.next
            l1=l1.next
        
        while l2:
            value=l2.val+carry
            listval=value%10
            carry=value//10
            newNode= ListNode(listval)
            curr.next=newNode
            curr=curr.next
            l2=l2.next
        
        if carry:
            newNode=ListNode(carry)
            curr.next=newNode
        # TC O(N+M) AND SC O(1)
        return res.next
