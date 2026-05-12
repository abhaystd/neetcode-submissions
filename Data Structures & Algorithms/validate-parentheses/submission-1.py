class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        ope = ['{','[','(']
        clos = ['}',']',')']

        for c in s:
            if c in clos:
                if len(stack) !=0 and ((c == ')' and stack[-1] == '(') or 
                    (c == '}' and stack[-1] == '{') or (c == ']' and stack[-1] == '[')):
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if len(stack) == 0 else False