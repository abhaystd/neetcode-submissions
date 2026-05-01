class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return 'π'
        s=strs[0]
        for i in range(1,len(strs)):
            s=s+'é'+strs[i]

        return s

    def decode(self, s: str) -> List[str]:
        if s=='π':
            return []
        return s.split('é')

