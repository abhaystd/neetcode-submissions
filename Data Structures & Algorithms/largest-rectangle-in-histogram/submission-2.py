class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area=0
        for i in range(len(heights)):
            height=heights[i]
            r=i
            l=i
            while  r<len(heights) and height<=heights[r]:
                r+=1
            while l>=0 and height<=heights[l]:
                l-=1
            area=height * (r-l-1)
            max_area=max(max_area,area)
        # Brute Force TC O(n^2) ans SC O(1) 
        return max_area
