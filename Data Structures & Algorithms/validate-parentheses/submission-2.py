class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]

        for c in s:
            if len(stack) !=0 and ((c == ')' and stack[-1] == '(') or 
                (c == '}' and stack[-1] == '{') or (c == ']' and stack[-1] == '[')):
                stack.pop()
            elif c == ')' or c == '}' or c == ']':
                return False
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
        # TC O(n) and SC O(n)
        return True if len(stack) == 0 else False