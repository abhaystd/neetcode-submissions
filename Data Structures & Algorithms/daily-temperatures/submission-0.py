class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res=[]
        for i in range(0,len(temperatures)):
            count=0
            j=i+1
            while j<len(temperatures):
                if temperatures[i]<temperatures[j]:
                    break;
                count+=1
                j+=1
            count = 0 if j==len(temperatures) else count+1
            res.append(count)
        return res