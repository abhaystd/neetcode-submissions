class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        right_max_height=[0]*n

        
        for i in range(n-1,0,-1):
            right_max_height[i-1]=max(right_max_height[i],height[i])
        print(right_max_height)

        trapped_water=0
        max_height=height[0]
        for i in range(1,n):
            min_height=min(max_height,right_max_height[i])
            if height[i]<min_height:
                trapped_water += min_height-height[i]
            max_height=max(max_height,height[i])
        return trapped_water
