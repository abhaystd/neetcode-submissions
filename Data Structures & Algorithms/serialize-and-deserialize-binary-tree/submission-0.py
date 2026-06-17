# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        serializeStr=''
        q=deque()
        q.append(root)
        while q:
            l=len(q)
            for i in range(l):
                curr=q.popleft()
                serializeStr+=','+str(curr.val) if curr else ',None'
                if curr:
                    q.append(curr.left)
                    q.append(curr.right)
        # print(serializeStr)
        return serializeStr
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        nodes=data.split(',')
        print(nodes)
        
        if len(nodes)<2:
            return None
        root=TreeNode(int(nodes[1]))
        i=2
        q=deque()
        q.append(root)
        while i<len(nodes) and q:
            l=len(q)
            for j in range(l):
                curr=q.popleft()
                if nodes[i]!='None':
                    leftNode=TreeNode(int(nodes[i]))
                    curr.left=leftNode
                    q.append(leftNode)
                i+=1
                if nodes[i]!='None':
                    rightNode=TreeNode(int(nodes[i]))
                    curr.right=rightNode
                    q.append(rightNode)
                i+=1
        return root

