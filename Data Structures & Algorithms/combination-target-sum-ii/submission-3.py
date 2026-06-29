class Solution:
    def __init__(self):
        self.res=[]
    def calAllComb(self,candidates: List[int], target: int,i:int,comb:List[int],s:int):
        if target==s:
            self.res.append(comb.copy())
            return
        if i>=len(candidates) or target<s:
            return
        
        # inclusion
        comb.append(candidates[i])
        self.calAllComb(candidates,target,i+1,comb,s+candidates[i])
        # backtrack
        comb.pop()
        # skipping duplicate combinations
        while i+1<len(candidates)  and candidates[i]==candidates[i+1]:
            i+=1

        self.calAllComb(candidates,target,i+1,comb,s)


    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.calAllComb(candidates,target,0,[],0)
        # TC O(N*2^N) AND SC O(N)
        return self.res
