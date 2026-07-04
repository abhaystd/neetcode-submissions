class Solution:
    def __init__(self):
        self.res =[]
    def isPalind(self,s,l,r):
        while l<r:
            if s[l]!=s[r]:
                return False
            l,r=l+1,r-1
        return True
    def collectAllPal(self,s,pal,i):
        if i>=len(s):
            self.res.append(pal.copy())
            return
        for j in range(i,len(s)):
            if self.isPalind(s,i,j):
                pal.append(s[i:j+1])
                self.collectAllPal(s,pal,j+1)
                pal.pop()
        return 
    def partition(self, s: str) -> List[List[str]]:
        self.collectAllPal(s,[],0)
        return self.res
        