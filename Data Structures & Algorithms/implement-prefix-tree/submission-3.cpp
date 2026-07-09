class TrieNode{
public:
    TrieNode* child[26];
    bool endOfWord;

    TrieNode(){
        endOfWord=false;
        for (int i=0;i<26;i++){
            child[i]=nullptr;
        }
    }
};


class PrefixTree {
public:
    TrieNode* root;
    PrefixTree() {
        root=new TrieNode();
    }
    
    void insert(string word) {
        TrieNode* curr=root;
        for (char c:word){
            if (!curr->child[c-'a']){
                curr->child[c-'a']=new TrieNode();
            }
            curr=curr->child[c-'a'];
        }
        curr->endOfWord=true;
    }
    
    bool search(string word) {
        TrieNode* curr=root;
        for (char c:word){
            if (!curr->child[c-'a']){
                return false;
            }
            curr=curr->child[c-'a'];

        }
        return curr->endOfWord;
    }
    
    bool startsWith(string prefix) {
        TrieNode* curr=root;
        for (char c:prefix){
            if (!curr->child[c-'a']){
                return false;
            }
            curr=curr->child[c-'a'];

        }
        return true;
    }
};