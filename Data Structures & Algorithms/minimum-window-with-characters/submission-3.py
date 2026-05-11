class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=='':
            return ''

        freq=defaultdict(int)
        for c in t:
            freq[c] +=1 

        matched=0
        req=len(freq)

        res, reslen = [-1, -1], float('inf')
        freqs=defaultdict(int)
        l=0
        for i in range(len(s)):
            if freq[s[i]]!=0:
                freqs[s[i]]+=1
                if freqs[s[i]]==freq[s[i]]:
                    matched+=1

            while matched == req and l<=i:
                if reslen > i-l+1:
                    reslen = i-l+1  
                    res=[l,i]
                if freq[s[l]]!=0:
                    freqs[s[l]] -= 1
                    if freqs[s[l]] <freq[s[l]]:
                        matched-=1
                l+=1      

        l, r =res
        # TC O(n) and SC O(1) 
        # max freq and freqs lenght can be 52 chars by add upper and lower chars
        return s[l:r+1] if reslen != float('inf') else ''


            
            
            

