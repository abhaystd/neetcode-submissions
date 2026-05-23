class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums=[]
        l1=0
        l2=0
        while (l1<len(nums1) and l2<len(nums2)):
            if nums1[l1]<=nums2[l2]:
                nums.append(nums1[l1])
                l1+=1
            else:
                nums.append(nums2[l2])
                l2+=1

        while l2<len(nums2):
            nums.append(nums2[l2])
            l2+=1

        while l1<len(nums1):
            nums.append(nums1[l1])
            l1+=1

        n=len(nums)

        return ( (nums[n//2] + nums[n//2-1])/2) if (len(nums)%2==0 ) else nums[n//2]
