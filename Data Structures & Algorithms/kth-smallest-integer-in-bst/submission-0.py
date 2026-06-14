# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return -1
        count = k
        res = root.val
        def dfs(root):
            if not root:
                return
            nonlocal count
            nonlocal res

            
            dfs(root.left)
            if count == 0:
                return

            count -= 1

            if count == 0:
                res = root.val
                return
            dfs(root.right)
            
            return
        dfs(root)
        return res


