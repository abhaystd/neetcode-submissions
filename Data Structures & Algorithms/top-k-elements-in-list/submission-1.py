class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq=defaultdict(int)

        for i in nums:
            freq[i] +=1
        n=len(nums)
        freq_bucket=defaultdict(list)
        for i in range(0,n+1):
            freq_bucket[i]=[]
        for key,value in freq.items():
            freq_bucket[value].append(key)
        res=[]
        for i in range(n,0,-1):
           
            res.extend(freq_bucket[i])
            if len(res)==k:
                break;
        return res

