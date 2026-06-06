# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):

            if not root:
                return 0,True

            l,lv=dfs(root.left)
            r,rv=dfs(root.right)
            valid=lv and rv and abs(r-l)<=1
            return max(r,l)+1,valid
        # TC O(N) AND SC O(N)
        h, v = dfs(root)
        return v
