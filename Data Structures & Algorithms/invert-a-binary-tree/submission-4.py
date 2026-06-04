# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root

        queue=deque()
        queue.append(root)
        while queue:
            tempRoot=queue.popleft()
            l=tempRoot.left
            tempRoot.left=tempRoot.right
            tempRoot.right=l
            if tempRoot.left:
                queue.append(tempRoot.left)
            if tempRoot.right:
                queue.append(tempRoot.right)
        # bfs TC O(N) AND SC O(N)
        return root