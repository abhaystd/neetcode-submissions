# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        q=deque()
        res=0
        q.append((root,-float('inf')))
        while q:
            l=len(q)
            for i in range(l):
                curr,maxVal=q.popleft()
                if maxVal<=curr.val:
                    res+=1
                    maxVal=curr.val

                if curr.left:
                    q.append((curr.left,maxVal))
                if curr.right:
                    q.append((curr.right,maxVal))
        # DFS TC O(N) AND SC O(N)
        return res







