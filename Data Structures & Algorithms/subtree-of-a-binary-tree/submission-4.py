# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution: 
    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        def serialize(node):
            if not node:
                return ',#'
            return f",{node.val}"+serialize(node.left)+serialize(node.right)
        # TC O(M*N)  AND SC O(M+N)
        rt=serialize(root)
        srt=serialize(subRoot)
        # TC O(N+M) AND SC(N+M)
        return srt in rt

            