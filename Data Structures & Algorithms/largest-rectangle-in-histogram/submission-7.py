class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area=0
        stack=[]
        for i in range(len(heights)):
            while len(stack) and heights[stack[-1]]>heights[i]:
                height=heights[stack[-1]]
                stack.pop()
                prv_small_idx = stack[-1] if len(stack) else -1
                max_area=max(max_area,(height*(i-prv_small_idx -1)))

            stack.append(i)
        
        while len(stack):
            nexr_small_idx=len(heights)
            height=heights[stack[-1]]
            stack.pop()
            prv_small_idx= stack[-1] if len(stack) else -1
            max_area=max(max_area,(height*(nexr_small_idx - prv_small_idx -1)))
        # TC O(2n) and SC O(n)
        return max_area
