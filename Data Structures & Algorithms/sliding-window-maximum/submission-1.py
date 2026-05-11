class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq=deque()
        l=0
        res=[]
        for i in range(len(nums)):
            while len(dq)!=0 and nums[i]>nums[dq[-1]]:
                dq.pop()
            dq.append(i)
            while i-l+1>k and l<i:
                if dq[0]<=l:
                    dq.popleft()
                l+=1
            if i-l+1==k:
                res.append(nums[dq[0]])
        # TC O(n) and SC T(n)
        return res
