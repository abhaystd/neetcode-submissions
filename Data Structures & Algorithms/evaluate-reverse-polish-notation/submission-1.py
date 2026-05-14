class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for s in tokens:
            if s in ['*','-','+','/']:
                top_val=stack[-1]
                stack.pop()
                top_second=stack[-1]
                stack.pop()
                if s=='-':
                    opp_res=top_second - top_val
                elif s=='+':
                    opp_res= top_second + top_val
                elif s=='*':
                    opp_res=top_second * top_val
                elif s=='/':
                    opp_res=top_second // top_val
                    float_value=top_second / top_val
                    if opp_res < 0 and opp_res<float_value:
                        opp_res=opp_res+1

                stack.append(opp_res)
            else:
                stack.append(int(s))
        return stack[-1]
            
            