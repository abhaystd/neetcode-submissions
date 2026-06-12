# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findGoodnodes(self, root: TreeNode,maxNode: int) -> val:
        if not root:
            return 0
        print(root.val,maxNode)
        maxvalue=max(maxNode,root.val)
        l=self.findGoodnodes(root.left,maxvalue)
        r=self.findGoodnodes(root.right,maxvalue)

        return (l+r+1) if root.val >= maxvalue else (r+l)
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        # DFS TC O(N) AND SC O(N)
        return self.findGoodnodes(root,root.val)







