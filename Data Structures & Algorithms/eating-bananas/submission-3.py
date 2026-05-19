class Solution:
    def is_possible(self, mid:int, piles:List[int], h:int) ->bool:
        total_hours=0
        for pile in piles:
            total_hours+=(pile+mid-1)//mid
        return total_hours<=h
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_eat=max(piles)
        min_eat=1

        while min_eat<=max_eat:
            mid=(min_eat+max_eat)//2
            if self.is_possible(mid,piles,h):
                print(mid)
                max_eat = mid-1
            else:
                min_eat = mid+1
        # TC O(n log v)  where v is max value of pile and SC O(1)
        return min_eat

