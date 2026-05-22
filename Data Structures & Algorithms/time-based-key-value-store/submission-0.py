class TimeMap:

    def __init__(self):
        self.keyTimeMap= defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        timeMap=self.keyTimeMap
        timeMap[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        timeMap=self.keyTimeMap
        l=0
        values=timeMap.get(key,[])
        if len(values) ==0:
            return ''
        r=len(values)-1
        res=values[0][1]
        t=values[0][0]
        while l <= r:
            mid = (l+r)//2
            if timestamp>=values[mid][0]:
                l = mid+1
                t=values[mid][0]
                res = values[mid][1]
            else:
                r = mid-1
        return "" if t>timestamp else res


