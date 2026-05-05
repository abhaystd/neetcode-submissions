class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water=0
        l=0
        r=len(heights)-1
        while(l<r):
            min_height= heights[l] if heights[r]>heights[l] else heights[r]
            curr_water = min_height*(r-l)
            max_water = curr_water if curr_water>max_water else max_water
            if heights[l]<=heights[r]:
                l+=1
            else:
                r-=1
        # space complexity O(1) and time complexity O(n)
        return max_water
