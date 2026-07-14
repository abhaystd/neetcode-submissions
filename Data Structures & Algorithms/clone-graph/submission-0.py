"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node :
            return None
        old_to_new = {}

        res = Node(val=node.val)
        old_to_new[node]=res
        queue=deque()
        queue.append(node)

        while queue:

            curr=queue.popleft()

            for neighbour in curr.neighbors:

                if neighbour not in old_to_new:

                    newNode=Node(val=neighbour.val)
                    old_to_new[neighbour]=newNode

                    queue.append(neighbour)

                old_to_new[curr].neighbors.append(old_to_new[neighbour])

        return old_to_new[node]



