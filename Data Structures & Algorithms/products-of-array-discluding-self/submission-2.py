class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res=[1]*(n)

        for i in range(n-2,-1,-1):
            res[i]=res[i+1]*nums[i+1]

        prod=1
        for i in range(0,n):
            res[i]=prod*res[i]
            prod=prod*nums[i]
        
        return res