class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        l = 0

        freq = defaultdict(int)
        maxf=0
        for i in range(len(s)):
            freq[s[i]] += 1
            maxf = max(maxf, freq[s[i]])
            while (i+1-l) - maxf > k:
                freq[s[l]] -= 1
                l += 1

            res = max(res,i+1-l)
        # TC O(n) and SC O(N)
        return res

