# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        n = 0
        temp = head
        while temp:
            temp = temp.next
            n += 1
        if n < k:
            return head

        res = None
        temp = head
        tail = None
        while n >= k:
            prev=None
            temphead = temp
            l = k
            while l>0 and temp:
                nxt = temp.next
                temp.next = prev
                prev = temp
                temp = nxt
                l -= 1
            if not res:
                res = prev
                tail = temphead
            else:
                tail.next = prev
                tail = temphead
            n -= k
        if n>0:
            tail.next=temp
        return res
            




