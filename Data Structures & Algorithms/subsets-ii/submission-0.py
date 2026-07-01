class Solution:
    def __init__(self):
        self.res=[]
    def findAllSubsets(self,nums,sub,i):
        if len(nums)==i:
            self.res.append(sub.copy())
            return
        if len(nums)<i:
            return
        sub.append(nums[i])
        self.findAllSubsets(nums,sub,i+1)
        sub.pop()
        while (i+1)<len(nums) and nums[i]==nums[i+1]:
            i+=1
        self.findAllSubsets(nums,sub,i+1)
        return

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.findAllSubsets(nums,[],0)
        return self.res