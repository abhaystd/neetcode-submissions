class Solution:
    def __init__(self):
        self.res=[]
    def getAllSubeset(self,nums,sbst,i):
        # base case when i reached end of nums
        if i==len(nums):
            self.res.append(sbst.copy())
            return
        # inclusion case
        sbst.append(nums[i])
        self.getAllSubeset(nums,sbst,i+1)
        # bactracking so we can pass sbst for exclusion
        sbst.pop()
        # exclusion case
        self.getAllSubeset(nums,sbst,i+1)
        return
        
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.getAllSubeset(nums,[],0)
        # TC O(N*2^n) and SC O(n)
        return self.res