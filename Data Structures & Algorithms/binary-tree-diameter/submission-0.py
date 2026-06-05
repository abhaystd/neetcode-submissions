# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.d=0
    def calDia(self,root:Optional[TreeNode])->int:
        if not root:
            return 0
        l=self.calDia(root.left)
        r=self.calDia(root.right)
        
        self.d = max(self.d, r+l)
        return 1 + max(r,l)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.calDia(root)

        return self.d


