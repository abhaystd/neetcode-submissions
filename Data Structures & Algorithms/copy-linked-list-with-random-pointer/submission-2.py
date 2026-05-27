"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head

        temp=head
        idx=0
        while temp:
            newNode = Node(temp.val)
            nxt=temp.next
            temp.next=newNode
            newNode.next = nxt
            temp = nxt

        temp=head
        while temp and temp.next:
            if temp.random:
                temp.next.random=temp.random.next
            temp=temp.next.next
        temp=head
        second=head.next
        curr=head.next
        while temp and temp.next:
            tempnxt=temp.next.next
            currnxt=None
            if curr.next:
                currnxt=curr.next.next
            temp.next=tempnxt
            curr.next=currnxt
            temp=temp.next
            curr=curr.next
        return second
