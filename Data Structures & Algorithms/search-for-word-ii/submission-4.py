class TrieNode:
    def __init__(self):
        self.child = {}
        self.isWord = False
    def addWord(self,word):
        curr=self
        for c in word:
            if c not in curr.child:
                curr.child[c]=TrieNode()
            curr=curr.child[c]
        curr.isWord=True


class Solution:

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        row=len(board)
        col=len(board[0])
        root = TrieNode()
        for word in words:
            root.addWord(word)

        res=set()
        vis=set()
        def dfs(r,c,node,word):
            if r>=row or r<0 or c>=col or c<0 or (r,c) in vis or board[r][c] not in node.child:
                return
            vis.add((r,c))
            node = node.child[board[r][c]]
            word+=board[r][c]
            if node.isWord:
                res.add(word)
            
            dfs(r+1,c,node,word)
            dfs(r-1,c,node,word)
            dfs(r,c+1,node,word)
            dfs(r,c-1,node,word)
            vis.remove((r,c))

        for r in range(len(board)):
            for c in range(len(board[0])):
                dfs(r,c,root,'')
        return list(res)


        