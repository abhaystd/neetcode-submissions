class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq=defaultdict(int)

        for i in nums:
            freq[i] +=1

        sorted_by_value=dict(sorted(freq.items(), key = lambda item:item[1], reverse=True))
        res=[]
        print(sorted_by_value)
        i=0
        for key,_ in sorted_by_value.items():
            if i==k:
                break;
            i+=1
            res.append(key)
        return res

