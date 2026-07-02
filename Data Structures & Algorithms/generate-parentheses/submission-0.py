class Solution:
    def __init__(self):
        self.res=[]
    def generateALL(self,comb: List[str],o:int,c:int,n:int):
        if o==n and c==n:
            self.res.append("".join(comb))
            return
        
        if o<n:
            comb.append('(')
            self.generateALL(comb,o+1,c,n)
            comb.pop()
        if c<o:
            comb.append(')')
            self.generateALL(comb,o,c+1,n)
            comb.pop()

        return

    def generateParenthesis(self, n: int) -> List[str]:
        self.generateALL([],0,0,n)
        return self.res