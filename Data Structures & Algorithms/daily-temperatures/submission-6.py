class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n=len(temperatures)
        stack=[]
        res=[0]*n
        for i in range(n):
            while len(stack) and temperatures[i]>temperatures[stack[-1]]:
                days = (i - stack[-1] )
                res[stack[-1]]=days
                stack.pop()
            stack.append(i)

        # TC O(N) AND SC O(N)
        return res