class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # binary search
        l=0
        r=len(nums)-1

        if nums[0] > nums[-1]:
            while l<=r:
                mid=(l+r)//2
                if nums[mid]>nums[-1]:
                    l = mid+1
                else:
                    r=mid-1
            print(l)
            print(r)
            # if target==nums[l]:
            #     return l
            if target <= nums[l-1] and target >= nums[0]:
                l=0
            else:
                r=len(nums)-1
        
        while l<=r:
            mid=(l+r)//2
            if nums[mid]==target:
                return mid
            if nums[mid]>target:
                r = mid-1
            else:
                l=mid+1
        return -1


