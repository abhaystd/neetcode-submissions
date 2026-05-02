class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        right_to_left_mul=[1]*(n+1)
        print(right_to_left_mul)
        for i in range(n-1,-1,-1):
            right_to_left_mul[i]=right_to_left_mul[i+1]*nums[i]
        print(right_to_left_mul)
        res=[]
        prod=1
        for i in range(0,n):
            res.append(prod*right_to_left_mul[i+1])
            prod=prod*nums[i]
        
        return res