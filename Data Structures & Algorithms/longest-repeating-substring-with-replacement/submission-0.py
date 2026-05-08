class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res=0
        for i in range(len(s)):
            freq=defaultdict(int)
            maxf=0
            for j in range(i,len(s)):
                freq[s[j]]+=1
                maxf=max(maxf,freq[s[j]])
                if (j+1-i)-maxf <= k:
                    res=max(res, j+1-i)
        # Brute force
        return res
