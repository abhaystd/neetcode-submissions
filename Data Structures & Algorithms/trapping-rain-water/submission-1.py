class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        right_max_height=[0]*n
        # calculate max height at each index from right side
        for i in range(n-1,0,-1):
            right_max_height[i-1]=max(right_max_height[i],height[i])

        

        trapped_water=0
        max_height=height[0]
        for i in range(1,n):
            #cal min height at that position from left to right to fill water
            min_height=min(max_height,right_max_height[i]) 
            # if current position is less then both side then water can be filled
            if height[i]<min_height:
                trapped_water += min_height-height[i] #add water
            max_height=max(max_height,height[i]) #update left max height

        # Time complexity TC O(n) and SC O(n)
        return trapped_water
