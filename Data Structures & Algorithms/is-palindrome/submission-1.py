class Solution:
    def isPalindrome(self, s: str) -> bool:

        alpha_num='abcdefghijklmnopqrstuvwxyz1234567890'
        fullstr=''
        for ch in s:
            fullstr+= ch.lower() if ch.lower() in alpha_num else ''
        
        n= len(fullstr)
        for i in range(0,n//2):
            if fullstr[i]!=fullstr[(n-1)-i]:
                return False
        return True
