class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res=0
        st=set()
        l=0
        for i in range(len(s)):
            while s[i] in st:
                st.discard(s[l])
                l+=1
            st.add(s[i])
            res=max(res,len(st))
        # TC O(n) and SC O(n)
        return res
        