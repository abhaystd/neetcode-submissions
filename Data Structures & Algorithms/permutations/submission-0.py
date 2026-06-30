class Solution:
    def __init__(self):
        self.res=[]
    def find_All_per(self,nums,flag,per):
        if len(per)==len(nums):
            self.res.append(per[:])
            return
        for i in range(len(nums)):
            if flag[i]:
                continue
            per.append(nums[i])
            flag[i]=True
            self.find_All_per(nums,flag,per)
            per.pop()
            flag[i]=False

    def permute(self, nums: List[int]) -> List[List[int]]:
        self.find_All_per(nums,[False]*len(nums),[])
        return self.res