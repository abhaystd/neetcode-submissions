class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        st=set()
        res=set()
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                rem=0-(nums[i]+nums[j])
                if rem in st:
                    triplet=[rem,nums[i],nums[j]]
                    triplet.sort()
                    res.add(tuple(triplet))

            st.add(nums[i])
        return list(res)
