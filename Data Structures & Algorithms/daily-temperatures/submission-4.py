class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n=len(temperatures)
        stack=[]
        res=[0]*n
        for i in range(n-1,-1,-1):
            while len(stack) and temperatures[i]>=temperatures[stack[-1]]:
                stack.pop()

            days = (stack[-1] - i )if len(stack) else 0
            res[i]=days
            stack.append(i)

        # TC O(N) AND SC O(N)
        return res