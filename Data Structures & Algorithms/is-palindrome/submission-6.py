class Solution:
    def isPalindrome(self, s: str) -> bool:

        l=0
        r=len(s)-1
        while l<=r:

            while r>=0 and not s[r].isalnum():
                r-=1
            while l<len(s) and not s[l].isalnum():
                l+=1
            if l<len(s) and r>=0 and s[r].lower()!=s[l].lower():
                return False
            else:
                l+=1
                r-=1

        return True
