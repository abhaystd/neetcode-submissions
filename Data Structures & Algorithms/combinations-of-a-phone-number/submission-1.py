class Solution:
    def __init__(self):
        self.res=[]
    def findALLComb(self,digits,comb,i,dig):
        if i>=len(digits):
            self.res.append(''.join(comb))
            return
        currstr=dig[digits[i]]
        comb.append(currstr[0])
        self.findALLComb(digits,comb,i+1,dig)

        comb.pop()
        comb.append(currstr[1])
        self.findALLComb(digits,comb,i+1,dig)

        comb.pop()
        comb.append(currstr[2])
        self.findALLComb(digits,comb,i+1,dig)
        comb.pop()
        if len(currstr)>3:
            
            comb.append(currstr[3])
            self.findALLComb(digits,comb,i+1,dig)
            comb.pop()
        return

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        dig={
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz',
        }
        self.findALLComb(digits,[],0,dig)
        
        return self.res