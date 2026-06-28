class Solution:
    def __init__(self):
        self.res=[]
    def finfComb(self,nums,target,comb,s,i):
        if target==s:
            self.res.append(comb.copy())
            return
        if target<s or i>=len(nums):
            return
        # next choose
        comb.append(nums[i])
        self.finfComb(nums,target,comb,s+nums[i],i)
        comb.pop()
        # same choose

        self.finfComb(nums,target,comb,s,i+1)

        return 

    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.finfComb(nums,target,[],0,0)
        return self.res