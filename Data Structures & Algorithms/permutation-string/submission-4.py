class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq=[0]*26
        l1=len(s1)
        l2=len(s2)
        if l1>l2:
            return False
        for s in s1:
            freq[ord(s)-ord('a')]+=1
        freq2=[0]*26

        for i in range(0,l1):
            freq2[ord(s2[i]) - ord('a')]+=1
        matched = 0
        for i in range(0,26):
            if freq[i]==freq2[i]:
                matched +=1
        if matched == 26:
            return True
        l=0
        i=l1

        while i<l2 :
            left_index = ord(s2[l])-ord('a')

            freq2[left_index]-=1
            if freq[left_index] == freq2[left_index]:
                matched +=1
            elif freq[left_index] - 1 == freq2[left_index]:
                matched -=1

            curr_index = ord(s2[i])-ord('a')
            freq2[curr_index]+=1
            if freq[curr_index] == freq2[curr_index]:
                matched +=1
            elif freq[curr_index] + 1 == freq2[curr_index]:
                matched -=1

            if matched == 26:
                return True
            l+=1
            i+=1
        # TC O(n) where n is max length of s1 or s2 string
        # SC O(1)
        return False
            
            





