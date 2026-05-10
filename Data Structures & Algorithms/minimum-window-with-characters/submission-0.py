class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=='':
            return ''

        freq=defaultdict(int)
        for c in t:
            freq[c] +=1 
        
        res, reslen = [-1, -1], float('inf')
        for i in range(len(s)):
            counts=defaultdict(int)
            for j in range(i,len(s)):
                counts[s[j]] +=1
                flag =True

                for c in freq:
                    if freq[c]>counts[c]:
                        flag =False
                        break
                if flag and (j-i+1)<reslen:
                    reslen=j-i+1
                    res=[i, j]
        l, r =res
        return s[l:r+1] if reslen != float('inf') else ''


            
            
            

