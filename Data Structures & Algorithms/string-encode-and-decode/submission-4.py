class Solution:

    def encode(self, strs: List[str]) -> str:
        strs_len=[]
        strs_len.append(str(len(strs)))
        strs_len.append('#')
        for st in strs:
            strs_len.append(str(len(st)))
            strs_len.append('#')

        en_mess=''.join(strs_len)
        for st in strs:
            en_mess=en_mess+st
        # print(en_mess)
        return en_mess

    def decode(self, s: str) -> List[str]:
        list_len=''
        start_point=0
        for i in s:
            start_point+=1
            if i=='#':
                break
            list_len=list_len+i
        list_len=int(list_len)

        hash_count=1
        string_list_len=[]
        val=''
        start=start_point-1
        for i in range(start_point,len(s)):
            start=start+1
            if hash_count == list_len+1:
                break;
            if s[i]=='#':
                string_list_len.append(int(val))
                val=''
                hash_count+=1
            else:
                val=val+s[i]
        print(string_list_len)
        res=[]
        for num in string_list_len:
            end=start+num
            res.append(s[start:end])
            start=end
        return res

