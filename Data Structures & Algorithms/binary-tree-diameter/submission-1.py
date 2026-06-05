# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        d=0
        def dfs(root):
            nonlocal d

            if not root:
                return 0
            l=dfs(root.left)
            r=dfs(root.right)

            d=max(d,r+l)

            return 1+max(l,r)
        dfs(root)
        return d


