# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        q1=deque()
        q2=deque()
        q1.append(p)
        q2.append(q)
        while q1 and q2:
            node1,node2=q1.popleft(),q2.popleft()
            if not node1 and not node2:
                continue
            if not node1 or not node2 or node1.val !=node2.val:
                return False
            q1.append(node1.right)
            q1.append(node1.left)
            q2.append(node2.right)
            q2.append(node2.left)
        if q1 or q2:
            return False
        # BFS tc O(N) AND SC O(N)
        return True 
