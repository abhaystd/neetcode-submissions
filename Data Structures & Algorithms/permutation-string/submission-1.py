class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq=[0]*26
        l1=len(s1)
        l2=len(s2)
        for s in s1:
            freq[ord(s)-ord('a')]+=1
        freq2=[0]*26
        l=0
        i=0
        while i<l2 :
            freq2[ord(s2[i])-ord('a')]+=1
            while i-l+1>l1 and i<l2:
                freq2[ord(s2[l])-ord('a')]-=1
                l+=1

            if i-l+1==l1 and freq == freq2:
                return True
            i+=1
        # TC O(n) where n is max length of s1 or s2 string
        # SC O(1)
        return False
            
            





