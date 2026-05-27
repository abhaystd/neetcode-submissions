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

        randomdict = defaultdict(Node)
        temp=head
        idx=0
        while temp:
            newNode = Node(temp.val)
            randomdict[temp]=newNode
            temp = temp.next

        temp = head
        idx=0

        while temp:
            if temp.next:
                randomdict[temp].next=randomdict[temp.next]
            if temp.random:
                randomdict[temp].random=randomdict[temp.random]
            temp = temp.next

        return randomdict[head]
            
