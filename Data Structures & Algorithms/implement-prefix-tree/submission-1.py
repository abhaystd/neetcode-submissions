class TrieNode:
    def __init__(self):
        self.child=[None]*26
        self.endWord=False

class PrefixTree:

    def __init__(self):
        self.root=TrieNode()

    def insert(self, word: str) -> None:
        curr=self.root

        for c in word:
            idx=ord(c)-ord('a')
            if not curr.child[idx]:
                curr.child[idx]=TrieNode()
            curr=curr.child[idx]
        
        curr.endWord=True

    def search(self, word: str) -> bool:
        curr=self.root
        for c in word:
            if not curr.child[ord(c)-ord('a')]:
                return False
            curr=curr.child[ord(c)-ord('a')]
        return curr.endWord
        

    def startsWith(self, prefix: str) -> bool:
        curr=self.root
        i=0
        for c in prefix:
            if not curr.child[ord(c)-ord('a')]:
                return False
            curr=curr.child[ord(c)-ord('a')]
        return True
        
        