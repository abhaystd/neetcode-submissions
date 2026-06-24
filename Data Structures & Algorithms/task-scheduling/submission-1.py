from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq=Counter(tasks)
        max_freq=0
        max_key=None
        for key,value in freq.items():
            if max_freq<value:
                max_freq=value
                max_key=key
        ideal=(max_freq-1)*n
        for key,value in freq.items():
            if max_key==key:
                continue
            ideal -= min(max_freq-1,value)
        # TC O(N) AND SC O(1)
        return max(0,ideal)+len(tasks)
