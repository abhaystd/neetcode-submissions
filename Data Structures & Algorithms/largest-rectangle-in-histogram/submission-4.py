class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area=0
        n=len(heights)
        r_index=[0]*n
        stack=[]
        for i in range(n):
            while len(stack) and heights[stack[-1]]>heights[i]:
                r_index[stack[-1]] = i-1
                stack.pop()
            stack.append(i)
        
        while len(stack):
            r_index[stack[-1]] = n-1
            stack.pop()
            
        l_index=[0]*n
        l_index[n-1]=n-1
        for i in range(n-1,-1,-1):

            while len(stack) and heights[stack[-1]]>heights[i]:
                l_index[stack[-1]] = i+1
                stack.pop()

            stack.append(i)
        
        while len(stack):
            l_index[stack[-1]] = 0
            stack.pop()
        print(r_index)
        print(l_index)
        for i in range(len(heights)):
            height=heights[i]
            r=r_index[i]
            l=l_index[i]
            area=height * (r-l+1)
            max_area=max(max_area,area)
        # Brute Force TC O(n^2) ans SC O(1) 
        return max_area
