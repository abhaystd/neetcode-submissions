class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res=0
        st=set()
        l=0
        for i in range(len(s)):
            if s[i] in st:
                while s[i] in st:
                    st.discard(s[l])
                    l+=1
            st.add(s[i])
            res=max(res,len(st))
        return res
        