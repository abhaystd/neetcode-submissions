class TrieNode:
    def __init__(self):
        self.child=[None]*26
        self.endWord=False
class WordDictionary:

    def __init__(self):
        self.root=TrieNode()
        
    
    def addWord(self, word: str) -> None:
        curr=self.root
        for c in word:
            if not curr.child[ord(c)-ord('a')]:
                curr.child[ord(c)-ord('a')]=TrieNode()
            curr=curr.child[ord(c)-ord('a')]
        
        curr.endWord=True

    def helper(self,root,word,idx):
        if idx==len(word) and root and root.endWord:
            return True
        if idx>=len(word) or not root:
            return False

        is_have=False
        if word[idx]=='.':
            for node in root.child:
                if node:
                    is_have = is_have or self.helper(node,word,idx+1)
        else:
            is_have = is_have or self.helper(root.child[ord(word[idx])-ord('a')],word,idx+1)
        return is_have
    def search(self, word: str) -> bool:
        return self.helper(self.root,word,0)

    # TC for add word O(n) length of word
    # TC for search word O(n) lenght of word if no wildcard and if all are wild card O(26^n)
    # SC O(m*n) here m is no words
        
