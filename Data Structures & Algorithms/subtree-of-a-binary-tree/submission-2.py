# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution: 
    def checkPossibility(self,temp,subRoot):
        if not temp and not subRoot:
            return True
        if not temp or not subRoot or temp.val != subRoot.val:
            return False
        return self.checkPossibility(temp.left,subRoot.left) and self.checkPossibility(temp.right,subRoot.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        if not root and subRoot:
            return False
        if root.val == subRoot.val:
            flag = self.checkPossibility(root,subRoot)
            if flag:
                return True
        # TC O(M*N)  AND SC O(M+N)
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)

            