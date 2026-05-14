class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for s in tokens:
            if s=='-':
                top_val, top_second=stack.pop() , stack.pop()
                opp_res=top_second - top_val
                stack.append(opp_res)
            elif s=='+':
                top_val, top_second=stack.pop() , stack.pop()
                opp_res= top_second + top_val
                stack.append(opp_res)
            elif s =='*':
                top_val, top_second = stack.pop(), stack.pop()
                opp_res=top_second * top_val
                stack.append(opp_res)
            elif s=='/':
                top_val, top_second=stack.pop() , stack.pop()
                float_value=top_second / top_val
                stack.append(int(float_value))
            else:
                stack.append(int(s))
        # TC O(n) and SC O(n)
        return stack[-1]
            
            