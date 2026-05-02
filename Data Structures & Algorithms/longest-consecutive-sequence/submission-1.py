class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        st=set()
        for num in nums:
            st.add(num)
        start_point=[]
        for num in nums:
            if (num-1) not in st:
                start_point.append(num)
        
        max_sec=0
        for num in start_point:
            curr_sec=1
            val=num+1
            while val in st:
                curr_sec +=1
                val+=1

            max_sec=max(max_sec,curr_sec)
            
        return max_sec